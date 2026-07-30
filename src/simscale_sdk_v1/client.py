"""Thin HTTP client wrapping httpx for the SimScale API."""

from __future__ import annotations

import logging
import threading
import time
import weakref
from collections.abc import Callable
from importlib.metadata import version
from pathlib import Path
from typing import Any, BinaryIO, Generic, TypeVar

import httpx
from pydantic import BaseModel, TypeAdapter

from simscale_sdk_v1.strip_unset import strip_unset_defaults

_SDK_VERSION = version("simscale_sdk_v1")
_USER_AGENT = f"simscale-sdk-python/{_SDK_VERSION}"

_RETRIABLE_STATUSES = frozenset({408, 429, 500, 502, 503, 504})
_IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})

logger = logging.getLogger("simscale_sdk_v1")

T = TypeVar("T", bound=BaseModel)


class _RateLimiter:
    """Thread-safe rate limiter spacing this client's outbound requests to at
    most rate_per_second (including retries), so a burst of concurrent calls
    stays under the server/WAF per-IP limit. A no-op when rate_per_second is
    None (the default), so existing callers are unaffected.
    """

    def __init__(self, rate_per_second: float | None) -> None:
        self._rate = rate_per_second
        self._min_interval = 1.0 / rate_per_second if rate_per_second and rate_per_second > 0 else None
        self._next = time.monotonic()
        self._lock = threading.Lock()

    def acquire(self) -> None:
        if self._min_interval is None:
            return
        with self._lock:
            now = time.monotonic()
            wait = self._next - now
            self._next = max(now, self._next) + self._min_interval
        if wait > 0:
            time.sleep(wait)


class PaginatedResponse(Generic[T]):
    """Generic paginated response for list endpoints returning _embedded/_meta."""

    def __init__(self, data: dict, item_type: type[T]) -> None:
        raw = data.get("_embedded", [])
        if isinstance(item_type, type) and issubclass(item_type, BaseModel):
            self.embedded: list[T] = [item_type.model_validate(item) for item in raw]
        else:
            # item_type is a type alias (e.g., Annotated union) — use TypeAdapter
            adapter = TypeAdapter(item_type)
            self.embedded = [adapter.validate_python(item) for item in raw]
        self.total: int = data.get("_meta", {}).get("total", 0)
        self.links: dict = data.get("_links", {})


class SimScaleOperationError(Exception):
    """Raised when an operation fails or a setup check has errors."""

    def __init__(self, result: Any, message: str = "Operation failed") -> None:
        self.result = result
        self.status = getattr(result, "status", None)
        super().__init__(self._format_message(message))

    def _format_message(self, message: str) -> str:
        lines = [message]
        if self.status:
            lines[0] += f" (status: {self.status})"
        reason = getattr(self.result, "failure_reason", None)
        if reason:
            lines.append(f"  {reason}")
        for entry in getattr(self.result, "entries", None) or []:
            severity = getattr(entry, "severity", None)
            code = getattr(entry, "code", None)
            msg = getattr(entry, "message", None)
            entry_line = " ".join(filter(None, [severity, f"{code}:" if code and msg else code, msg]))
            if entry_line:
                lines.append(f"  {entry_line}")
        return "\n".join(lines)


class SimScaleAPIError(Exception):
    """Raised when the SimScale API returns a non-2xx response."""

    def __init__(self, status_code: int, body: Any, response: httpx.Response) -> None:
        self.status_code = status_code
        self.body = body
        self.response = response
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        import http.client

        reason = http.client.responses.get(self.status_code, "Unknown")
        url = str(self.response.request.url)
        if isinstance(self.body, dict):
            lines = [str(self.body), ""]
            lines.append(f"{self.status_code} {reason}: {url}")
            severity = self.body.get("severity")
            code = self.body.get("code")
            message = self.body.get("message")
            main = " ".join(filter(None, [severity, f"{code}:" if code and message else code, message]))
            if main:
                lines.append(f"  {main}")
            for entry in self.body.get("entries") or []:
                e_sev = entry.get("severity")
                e_code = entry.get("code")
                e_msg = entry.get("message")
                entry_line = " ".join(filter(None, [e_sev, f"{e_code}:" if e_code and e_msg else e_code, e_msg]))
                if entry_line and entry_line != main:
                    lines.append(f"  {entry_line}")
            trace = self.body.get("trace")
            if trace:
                lines.append(f"  (trace: {trace})")
            return "\n".join(lines)
        return f"{self.status_code} {reason}: {url}\n  {self.body}"


class SimScaleTimeoutError(Exception):
    """Raised when a request exhausts its retries on client-side timeouts.

    Fail loud instead of hanging: carries the request context (method, url,
    elapsed, attempts) so a stuck call surfaces as a clear, actionable error
    rather than looking like a hang. Chained from the underlying httpx timeout.
    """

    def __init__(self, method: str, url: str, elapsed: float, attempts: int, cause: Exception) -> None:
        self.method = method
        self.url = url
        self.elapsed = elapsed
        self.attempts = attempts
        super().__init__(f"{method} {url} timed out after {attempts} attempt(s), {elapsed:.1f}s total: {cause}")


class SimScaleClient:
    """Low-level HTTP client for the SimScale v1 API."""

    def __init__(
        self,
        *,
        api_key: str,
        server_url: str,
        timeout: float = 60.0,
        max_retries: int = 5,
        retry_backoff: float = 0.2,
        retry_after_cap: float = 60.0,
        max_connections: int = 100,
        max_requests_per_second: float | None = None,
    ) -> None:
        self._server_url = server_url.rstrip("/")
        self._http = httpx.Client(
            base_url=self._server_url,
            headers={"X-API-KEY": api_key, "User-Agent": _USER_AGENT},
            follow_redirects=True,
            timeout=timeout,
            limits=httpx.Limits(max_connections=max_connections),
        )
        self._max_retries = max_retries
        self._retry_backoff = retry_backoff
        self._retry_after_cap = retry_after_cap
        self._rate_limiter = _RateLimiter(max_requests_per_second)
        # Safety net: close the httpx client (releasing its socket pool) if this
        # instance is garbage-collected without an explicit close()/context-exit.
        # Binds the client's close, not self, so it doesn't keep self alive.
        self._finalizer = weakref.finalize(self, self._http.close)

    def _with_retry(self, method: str, send: Callable[[], httpx.Response]) -> httpx.Response:
        """Invoke *send* with retries on transient failures.

        Retries network errors and 5xx responses for idempotent methods, and 429
        regardless of method (rate-limit — server hasn't acted yet). Honors
        Retry-After on 429 when present, capped at retry_after_cap. Disabled when
        max_retries is 0. Fails loud: a client timeout that exhausts retries is
        re-raised as SimScaleTimeoutError with context (never swallowed), and
        every retry is logged so a throttled/slow call is visible, not a hang.
        """
        method_u = method.upper()
        last_exc: Exception | None = None
        start = time.monotonic()
        for attempt in range(self._max_retries + 1):
            self._rate_limiter.acquire()
            try:
                resp = send()
            except (httpx.TimeoutException, httpx.NetworkError) as e:
                last_exc = e
                if attempt >= self._max_retries or method_u not in _IDEMPOTENT_METHODS:
                    if isinstance(e, httpx.TimeoutException):
                        # Use the private _request: the public .request property
                        # raises RuntimeError (not AttributeError) when unset, which
                        # getattr wouldn't swallow and would mask the timeout.
                        req = getattr(e, "_request", None)
                        raise SimScaleTimeoutError(
                            method_u,
                            str(getattr(req, "url", "?")),
                            time.monotonic() - start,
                            attempt + 1,
                            e,
                        ) from e
                    raise
                delay = self._retry_backoff * (2**attempt)
                logger.warning(
                    "%s request failed (%s); retry %d/%d in %.1fs",
                    method_u,
                    type(e).__name__,
                    attempt + 1,
                    self._max_retries,
                    delay,
                )
                time.sleep(delay)
                continue

            status = resp.status_code
            retry_status = status == 429 or (status in _RETRIABLE_STATUSES and method_u in _IDEMPOTENT_METHODS)
            if retry_status and attempt < self._max_retries:
                delay = self._retry_delay(attempt, resp)
                logger.warning(
                    "%s got HTTP %d; retry %d/%d in %.1fs",
                    method_u,
                    status,
                    attempt + 1,
                    self._max_retries,
                    delay,
                )
                time.sleep(delay)
                continue
            return resp
        raise last_exc if last_exc else RuntimeError("retry loop exited unexpectedly")

    def _retry_delay(self, attempt: int, resp: httpx.Response) -> float:
        if resp.status_code == 429:
            ra = resp.headers.get("Retry-After")
            if ra:
                try:
                    # Cap the server-provided delay so a large Retry-After doesn't
                    # stall the caller for minutes and read as a hang.
                    return min(max(0.0, float(ra)), self._retry_after_cap)
                except ValueError:
                    pass  # fall through to exponential backoff
        return self._retry_backoff * (2**attempt)

    @staticmethod
    def _serialize_model(model: BaseModel) -> dict:
        """Deep-copy, strip unset optional fields, and serialize to a JSON-compatible dict."""
        copy = model.model_copy(deep=True)
        strip_unset_defaults(copy)
        return copy.model_dump(by_alias=True, exclude_none=True, mode="json")

    def request(
        self,
        method: str,
        path: str,
        *,
        json_body: BaseModel | dict | list | None = None,
        binary_body: bytes | BinaryIO | Path | None = None,
        content_type: str | None = None,
        query_params: dict[str, Any] | None = None,
        response_type: type[T] | None = None,
        response_binary: bool = False,
    ) -> T | dict | bytes | None:
        """Send an HTTP request and optionally parse the JSON response into *response_type*.

        Accepts any 2xx status. Raises SimScaleAPIError on 4xx/5xx.
        """
        # Serialize Pydantic models to dict (by alias), stripping unset optional fields.
        # strip_unset_defaults nulls out optional fields the user didn't set (to avoid
        # conditional validation errors), while keeping non-optional defaults like "version".
        # exclude_none then drops the nulled-out fields from the JSON payload.
        json_data: Any = None
        if json_body is not None:
            if isinstance(json_body, BaseModel):
                json_data = self._serialize_model(json_body)
            elif isinstance(json_body, list):
                json_data = [self._serialize_model(item) if isinstance(item, BaseModel) else item for item in json_body]
            else:
                json_data = json_body

        if json_body is not None and binary_body is not None:
            raise ValueError("json_body and binary_body cannot be used together")

        # Strip None values from query params
        params = {k: v for k, v in (query_params or {}).items() if v is not None}

        headers = {"Content-Type": content_type} if content_type is not None else None
        if isinstance(binary_body, Path):

            def send_binary_file() -> httpx.Response:
                with binary_body.open("rb") as f:
                    return self._http.request(
                        method,
                        path,
                        content=f,
                        headers=headers,
                        params=params or None,
                    )

            resp = self._with_retry(method, send_binary_file)
        elif binary_body is not None:

            def send_binary_content() -> httpx.Response:
                if hasattr(binary_body, "seek"):
                    binary_body.seek(0)
                return self._http.request(
                    method,
                    path,
                    content=binary_body,
                    headers=headers,
                    params=params or None,
                )

            resp = self._with_retry(method, send_binary_content)
        else:
            resp = self._with_retry(
                method,
                lambda: self._http.request(method, path, json=json_data, params=params or None),
            )

        if not (200 <= resp.status_code < 300):
            try:
                body = resp.json()
            except Exception:
                body = resp.text
            raise SimScaleAPIError(resp.status_code, body, resp)

        if resp.status_code == 204 or not resp.content:
            return None

        if response_binary:
            return resp.content

        data = resp.json()
        if response_type is None:
            return data
        if isinstance(response_type, type) and issubclass(response_type, BaseModel):
            return response_type.model_validate(data)
        # Type alias (e.g. list[AiUserModel] from a top-level array schema) — use TypeAdapter
        return TypeAdapter(response_type).validate_python(data)

    def upload_to_storage(self, url: str, filepath: str | Path) -> None:
        """Upload a file to a presigned storage URL.

        Uses a plain HTTP client without API key headers since the URL points to
        an external storage host.
        """
        file_size = Path(filepath).stat().st_size

        def send() -> httpx.Response:
            with open(filepath, "rb") as f:
                return httpx.put(
                    url,
                    content=f,
                    headers={
                        "Content-Type": "application/octet-stream",
                        "Content-Length": str(file_size),
                        "User-Agent": _USER_AGENT,
                    },
                    timeout=300.0,
                )

        resp = self._with_retry("PUT", send)
        if not (200 <= resp.status_code < 300):
            raise SimScaleAPIError(resp.status_code, resp.text, resp)

    def download(self, url: str, filepath: str | Path) -> None:
        """Download a file from a URL to a local path.

        Uses a plain HTTP client without API key headers since the URL may point
        to an external host.
        """
        resp = self._with_retry(
            "GET",
            lambda: httpx.get(url, follow_redirects=True, headers={"User-Agent": _USER_AGENT}),
        )
        if not (200 <= resp.status_code < 300):
            raise SimScaleAPIError(resp.status_code, resp.text, resp)
        with open(filepath, "wb") as f:
            f.write(resp.content)

    def close(self) -> None:
        self._http.close()
