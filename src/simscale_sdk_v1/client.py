"""Thin HTTP client wrapping httpx for the SimScale API."""

from __future__ import annotations

import time
from collections.abc import Callable
from importlib.metadata import version
from pathlib import Path
from typing import Any, Generic, TypeVar

import httpx
from pydantic import BaseModel, TypeAdapter

from simscale_sdk_v1.strip_unset import strip_unset_defaults

_SDK_VERSION = version("simscale_sdk_v1")
_USER_AGENT = f"simscale-sdk-python/{_SDK_VERSION}"

_RETRIABLE_STATUSES = frozenset({408, 429, 500, 502, 503, 504})
_IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})

T = TypeVar("T", bound=BaseModel)


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


class SimScaleClient:
    """Low-level HTTP client for the SimScale v1 API."""

    def __init__(
        self,
        *,
        api_key: str,
        server_url: str,
        max_retries: int = 5,
        retry_backoff: float = 0.2,
    ) -> None:
        self._server_url = server_url.rstrip("/")
        self._http = httpx.Client(
            base_url=self._server_url,
            headers={"X-API-KEY": api_key, "User-Agent": _USER_AGENT},
            follow_redirects=True,
            timeout=30.0,
        )
        self._max_retries = max_retries
        self._retry_backoff = retry_backoff

    def _with_retry(self, method: str, send: Callable[[], httpx.Response]) -> httpx.Response:
        """Invoke *send* with retries on transient failures.

        Retries network errors and 5xx responses for idempotent methods, and 429
        regardless of method (rate-limit — server hasn't acted yet). Honors
        Retry-After on 429 when present. Disabled when max_retries is 0.
        """
        method_u = method.upper()
        last_exc: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                resp = send()
            except (httpx.TimeoutException, httpx.NetworkError) as e:
                last_exc = e
                if attempt >= self._max_retries or method_u not in _IDEMPOTENT_METHODS:
                    raise
                time.sleep(self._retry_backoff * (2**attempt))
                continue

            status = resp.status_code
            retry_status = status == 429 or (status in _RETRIABLE_STATUSES and method_u in _IDEMPOTENT_METHODS)
            if retry_status and attempt < self._max_retries:
                time.sleep(self._retry_delay(attempt, resp))
                continue
            return resp
        raise last_exc if last_exc else RuntimeError("retry loop exited unexpectedly")

    def _retry_delay(self, attempt: int, resp: httpx.Response) -> float:
        if resp.status_code == 429:
            ra = resp.headers.get("Retry-After")
            if ra:
                try:
                    return max(0.0, float(ra))
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
        query_params: dict[str, Any] | None = None,
        response_type: type[T] | None = None,
    ) -> T | dict | None:
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

        # Strip None values from query params
        params = {k: v for k, v in (query_params or {}).items() if v is not None}

        resp = self._with_retry(method, lambda: self._http.request(method, path, json=json_data, params=params or None))

        if not (200 <= resp.status_code < 300):
            try:
                body = resp.json()
            except Exception:
                body = resp.text
            raise SimScaleAPIError(resp.status_code, body, resp)

        if resp.status_code == 204 or not resp.content:
            return None

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
