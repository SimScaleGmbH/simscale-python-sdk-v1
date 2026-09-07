"""Network diagnostics for SDK environments.

Measures API roundtrip and storage upload throughput (single stream and
parallel) through the same upload-session path regular uploads use. Upload
sessions are deleted without finalizing, so nothing persists in the project.

Run via SimScaleSDK.network_check() or the simscale-network-check command.
"""

from __future__ import annotations

import ipaddress
import os
import platform
import socket
import ssl
import statistics
import sys
import time
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from dataclasses import asdict, dataclass, field
from importlib.metadata import version
from typing import TYPE_CHECKING
from urllib.parse import urlsplit

import httpx
import truststore

from simscale_sdk_v1 import models

if TYPE_CHECKING:
    from simscale_sdk_v1.models.data_repository import PresignedRequest
    from simscale_sdk_v1.sdk import SimScaleSDK

DEFAULT_PROJECT_NAME = "SimScale network check"

PROBE_BYTES = 4 * 1024 * 1024
TEST_SIZE_STEPS_BYTES = tuple(mib * 1024 * 1024 for mib in (8, 16, 32, 64, 128))
MAX_TEST_BYTES = TEST_SIZE_STEPS_BYTES[-1]

_DATA_TYPE = "simscale.file-formats:csv:1.0.0"
_CONTENT_TYPE = "application/octet-stream"
_TARGET_SECONDS = 8
_PARALLEL_STREAMS = 4
_RANDOM_BLOCK = os.urandom(64 * 1024)
_PROXY_ENV_VARS = (
    "HTTP_PROXY",
    "http_proxy",
    "HTTPS_PROXY",
    "https_proxy",
    "ALL_PROXY",
    "all_proxy",
    "NO_PROXY",
    "no_proxy",
)
_PUT_TIMEOUT = httpx.Timeout(3600.0, connect=30.0)


@dataclass
class NetworkCheckResult:
    api_url: str = ""
    sdk_version: str = ""
    python_version: str = ""
    httpx_version: str = ""
    operating_system: str = ""
    proxy_env: dict[str, str] = field(default_factory=dict)
    api_roundtrip_ms: float | None = None
    api_via_vpn: bool | None = None
    api_tls_issuer: str | None = None
    project_id: str | None = None
    project_created: bool | None = None
    storage_host: str | None = None
    storage_tcp_rtt_ms: float | None = None
    storage_tls_issuer: str | None = None
    storage_via_vpn: bool | None = None
    upload_single_mbits: float | None = None
    upload_single_test_bytes: int | None = None
    upload_parallel_mbits: float | None = None
    upload_parallel_streams: int | None = None
    upload_parallel_part_bytes: int | None = None
    effective_window_kib: float | None = None
    hints: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def _synthetic(size: int) -> Iterator[bytes]:
    remaining = size
    while remaining > 0:
        chunk = _RANDOM_BLOCK[: min(len(_RANDOM_BLOCK), remaining)]
        remaining -= len(chunk)
        yield chunk


def _source_ip(host: str) -> str:
    with socket.create_connection((host, 443), timeout=10) as connection:
        return connection.getsockname()[0]


def _is_vpn_source(ip: str) -> bool:
    # Tailscale and similar VPNs give the local interface an address from the CGNAT range.
    address = ipaddress.ip_address(ip)
    return address.version == 4 and address in ipaddress.ip_network("100.64.0.0/10")


def _tls_issuer(host: str) -> str:
    try:
        return _tls_issuer_with_context(host, truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT))
    except ssl.SSLCertVerificationError:
        # Retry with the bundled CA list; only a certificate neither the OS trust
        # store nor the bundle trusts indicates interception with an unknown CA.
        import certifi

        try:
            return _tls_issuer_with_context(host, ssl.create_default_context(cafile=certifi.where()))
        except ssl.SSLCertVerificationError as e:
            return f"untrusted certificate ({e.verify_message})"


def _tls_issuer_with_context(host: str, context: ssl.SSLContext) -> str:
    with (
        socket.create_connection((host, 443), timeout=10) as raw_socket,
        context.wrap_socket(raw_socket, server_hostname=host) as tls_socket,
    ):
        certificate = tls_socket.getpeercert()
    issuer = {key: value for pair in certificate.get("issuer", ()) for key, value in pair}
    return f"{issuer.get('commonName', 'unknown')} ({issuer.get('organizationName', 'unknown')})"


class NetworkCheck:
    def __init__(
        self,
        sdk: SimScaleSDK,
        *,
        project_id: str | None = None,
        max_tier_bytes: int | None = None,
        parallel_streams: int = _PARALLEL_STREAMS,
    ) -> None:
        self._sdk = sdk
        self._explicit_project_id = project_id
        self._max_tier_bytes = max_tier_bytes if max_tier_bytes is not None else MAX_TEST_BYTES
        self._parallel_streams = parallel_streams
        self._result = NetworkCheckResult()
        self._first_presigned_url: str | None = None

    def run(self) -> NetworkCheckResult:
        result = self._result
        self._environment()
        try:
            result.api_roundtrip_ms = self._api_roundtrip_ms()
        except Exception as e:
            result.errors.append(f"api-check: {e}")
            return result

        with suppress(Exception):
            api_host = urlsplit(result.api_url).hostname
            if api_host:
                result.api_via_vpn = _is_vpn_source(_source_ip(api_host))
                result.api_tls_issuer = _tls_issuer(api_host)

        try:
            result.project_id = self._resolve_project_id()
        except Exception as e:
            result.errors.append(f"project: {e}")
            return result

        try:
            self._measure_single_stream()
        except Exception as e:
            result.errors.append(f"upload-single: {e}")

        if self._first_presigned_url:
            try:
                self._storage_diagnostics(self._first_presigned_url)
            except Exception as e:
                result.errors.append(f"storage-diagnostics: {e}")

        if result.upload_single_mbits:
            try:
                self._measure_parallel()
            except Exception as e:
                result.errors.append(f"upload-parallel: {e}")

        self._derive()
        return result

    def _environment(self) -> None:
        result = self._result
        result.api_url = self._sdk._client._server_url
        result.sdk_version = version("simscale_sdk_v1")
        result.python_version = platform.python_version()
        result.httpx_version = httpx.__version__
        result.operating_system = f"{platform.system()} {platform.release()}"
        result.proxy_env = {name: os.environ[name] for name in _PROXY_ENV_VARS if name in os.environ}

    def _api_roundtrip_ms(self) -> float:
        self._sdk.users.get_current_user()
        timings = []
        for _ in range(3):
            start = time.monotonic()
            self._sdk.users.get_current_user()
            timings.append((time.monotonic() - start) * 1000)
        return statistics.median(timings)

    def _resolve_project_id(self) -> str:
        if self._explicit_project_id:
            return self._sdk.projects.get_project(self._explicit_project_id).project_id
        page = 1
        while True:
            response = self._sdk.projects.get_projects(limit=100, page=page)
            for project in response.embedded:
                if project.name == DEFAULT_PROJECT_NAME:
                    self._result.project_created = False
                    return project.project_id
            if page * 100 >= response.total or page >= 10:
                break
            page += 1
        project = self._sdk.projects.create_project(
            models.Project(
                name=DEFAULT_PROJECT_NAME,
                description="Created by simscale-network-check for upload throughput measurements. "
                "Nothing is stored here.",
                measurement_system="SI",
            ),
        )
        self._result.project_created = True
        return project.project_id

    def _create_session(self) -> str:
        session = self._sdk.data_repository.create_upload_session(
            models.data_repository.CreateUploadSessionRequest(
                data_type=_DATA_TYPE,
                content_type=_CONTENT_TYPE,
                original_file_name="network-check.bin",
            ),
            project_id=self._result.project_id,
        )
        if session.storage_id is None:
            raise RuntimeError("upload session response did not contain storage_id")
        return session.storage_id

    def _delete_session(self, storage_id: str) -> None:
        try:
            self._sdk.data_repository.delete_upload_session(storage_id, project_id=self._result.project_id)
        except Exception as e:
            self._result.errors.append(f"session-cleanup: {e}")

    def _start_append(self, storage_id: str, size: int):
        append = self._sdk.data_repository.start_upload_session_append(
            storage_id,
            models.data_repository.StartUploadSessionAppendRequest(size=size),
            project_id=self._result.project_id,
        )
        if (
            append.append_id is None
            or append.pre_signed_put_request is None
            or append.pre_signed_put_request.url is None
        ):
            raise RuntimeError("upload session append response was incomplete")
        if self._first_presigned_url is None:
            self._first_presigned_url = append.pre_signed_put_request.url
        return append

    def _timed_put_seconds(self, presigned: PresignedRequest, size: int) -> float:
        headers = {
            header.name: header.value
            for header in presigned.headers or []
            if header.name is not None and header.value is not None
        }
        headers.setdefault("Content-Length", str(size))
        start = time.monotonic()
        response = httpx.put(
            presigned.url, content=_synthetic(size), headers=headers, timeout=_PUT_TIMEOUT, follow_redirects=True
        )
        elapsed = time.monotonic() - start
        if not (200 <= response.status_code < 300):
            raise RuntimeError(f"presigned PUT failed: status {response.status_code}")
        return elapsed

    def _measure_append_mbits(self, storage_id: str, size: int) -> float:
        append = self._start_append(storage_id, size)
        try:
            elapsed = self._timed_put_seconds(append.pre_signed_put_request, size)
            self._sdk.data_repository.finish_upload_session_append(
                storage_id, append.append_id, project_id=self._result.project_id
            )
        except Exception:
            with suppress(Exception):
                self._sdk.data_repository.cancel_upload_session_append(
                    storage_id, append.append_id, project_id=self._result.project_id
                )
            raise
        return size * 8 / 1_000_000 / elapsed

    def _target_test_bytes(self, speed_mbits: float) -> int | None:
        # Largest power-of-two step that lasts about _TARGET_SECONDS at the measured rate.
        target = min(speed_mbits / 8 * 1_000_000 * _TARGET_SECONDS, self._max_tier_bytes)
        steps = [step for step in TEST_SIZE_STEPS_BYTES if step <= target]
        return steps[-1] if steps else None

    def _measure_single_stream(self) -> None:
        # Probe first, then measure again with a size chosen from the probed rate so the
        # transfer lasts several seconds: short transfers spend most of their time in TCP
        # ramp-up and understate the link. The second, longer run counts.
        result = self._result
        storage_id = self._create_session()
        try:
            size = min(PROBE_BYTES, self._max_tier_bytes)
            mbits = self._measure_append_mbits(storage_id, size)
            target = self._target_test_bytes(mbits)
            if target is not None:
                size = target
                mbits = self._measure_append_mbits(storage_id, size)
            result.upload_single_mbits = mbits
            result.upload_single_test_bytes = size
        finally:
            self._delete_session(storage_id)

    def _measure_parallel(self) -> None:
        # Transfer the single-stream test size again, split across the parallel streams.
        result = self._result
        part_bytes = max(PROBE_BYTES, (result.upload_single_test_bytes or PROBE_BYTES) // self._parallel_streams)
        part_bytes = min(part_bytes, self._max_tier_bytes)

        storage_ids = []
        try:
            for _ in range(self._parallel_streams):
                storage_ids.append(self._create_session())
            appends = [(storage_id, self._start_append(storage_id, part_bytes)) for storage_id in storage_ids]
            start = time.monotonic()
            with ThreadPoolExecutor(max_workers=self._parallel_streams) as pool:
                futures = [
                    pool.submit(self._timed_put_seconds, append.pre_signed_put_request, part_bytes)
                    for _, append in appends
                ]
                for future in futures:
                    future.result()
            elapsed = time.monotonic() - start
            for storage_id, append in appends:
                self._sdk.data_repository.finish_upload_session_append(
                    storage_id, append.append_id, project_id=result.project_id
                )
            result.upload_parallel_mbits = part_bytes * self._parallel_streams * 8 / 1_000_000 / elapsed
            result.upload_parallel_streams = self._parallel_streams
            result.upload_parallel_part_bytes = part_bytes
        finally:
            for storage_id in storage_ids:
                self._delete_session(storage_id)

    def _storage_diagnostics(self, presigned_url: str) -> None:
        result = self._result
        host = urlsplit(presigned_url).hostname
        if host is None:
            raise RuntimeError("presigned URL has no hostname")
        result.storage_host = host

        timings = []
        source_ip = None
        for _ in range(3):
            start = time.monotonic()
            with socket.create_connection((host, 443), timeout=10) as connection:
                timings.append((time.monotonic() - start) * 1000)
                if source_ip is None:
                    source_ip = connection.getsockname()[0]
        result.storage_tcp_rtt_ms = statistics.median(timings)
        result.storage_via_vpn = _is_vpn_source(source_ip) if source_ip else None

        result.storage_tls_issuer = _tls_issuer(host)

    def _derive(self) -> None:
        result = self._result
        if result.upload_single_mbits and result.storage_tcp_rtt_ms:
            bytes_per_second = result.upload_single_mbits * 1_000_000 / 8
            result.effective_window_kib = bytes_per_second * result.storage_tcp_rtt_ms / 1000 / 1024

        if result.proxy_env:
            names = ", ".join(sorted(result.proxy_env))
            result.hints.append(f"Proxy environment variables are set ({names}): traffic may pass a corporate proxy.")
        vpn_legs = [name for name, flag in (("API", result.api_via_vpn), ("storage", result.storage_via_vpn)) if flag]
        if vpn_legs:
            result.hints.append(
                f"{' and '.join(vpn_legs)} traffic routes through a VPN (source address in the CGNAT range, "
                "e.g. Tailscale): those measurements include the VPN path.",
            )
        for leg, issuer in (("API", result.api_tls_issuer), ("storage", result.storage_tls_issuer)):
            if issuer and "Amazon" not in issuer:
                result.hints.append(
                    f"The {leg} endpoint's TLS certificate is issued by '{issuer}', not by Amazon: "
                    "a TLS inspection appliance is likely in the path and typically limits throughput.",
                )


def _print_human(result: NetworkCheckResult) -> None:
    # Measurements first, environment details second, interpretation last.
    print("SimScale network check")
    print(
        f"  API:      {result.api_url}"
        + (f" (roundtrip {result.api_roundtrip_ms:.0f} ms)" if result.api_roundtrip_ms else "")
        + (" (via VPN)" if result.api_via_vpn else "")
    )
    if result.storage_host:
        print(
            f"  Storage:  {result.storage_host}"
            + (f" (TCP RTT {result.storage_tcp_rtt_ms:.1f} ms)" if result.storage_tcp_rtt_ms is not None else "")
            + (" (via VPN)" if result.storage_via_vpn else "")
        )
    if result.upload_single_mbits is not None:
        test_mib = result.upload_single_test_bytes // (1024 * 1024)
        print(f"  Upload:   single stream  {result.upload_single_mbits:.1f} Mbit/s ({test_mib} MiB)")
    if result.upload_parallel_mbits is not None:
        print(
            f"            {result.upload_parallel_streams} parallel     {result.upload_parallel_mbits:.1f} Mbit/s "
            f"({result.upload_parallel_streams} x {result.upload_parallel_part_bytes // (1024 * 1024)} MiB)",
        )
    if result.effective_window_kib is not None:
        print(f"  Effective TCP window: ~{result.effective_window_kib:.0f} KiB")

    print("\nEnvironment:")
    print(
        f"  SDK:      simscale-sdk-python/{result.sdk_version}, Python {result.python_version}, "
        f"httpx {result.httpx_version}, {result.operating_system}"
    )
    print(f"  Proxy:    {', '.join(sorted(result.proxy_env)) if result.proxy_env else 'none detected'}")
    issuers = []
    if result.api_tls_issuer:
        issuers.append(f"API {result.api_tls_issuer}")
    if result.storage_tls_issuer:
        issuers.append(f"storage {result.storage_tls_issuer}")
    if issuers:
        print(f"  TLS:      {', '.join(issuers)}")
    if result.project_id:
        note = " (new)" if result.project_created else " (existing)" if result.project_created is False else ""
        print(f"  Project:  {result.project_id}{note}")

    if result.hints:
        print("\nNotes:")
        for hint in result.hints:
            print(f"  - {hint}")
    if result.errors:
        print("\nErrors:")
        for error in result.errors:
            print(f"  - {error}")


def main() -> int:
    if len(sys.argv) > 1:
        print("simscale-network-check takes no arguments", file=sys.stderr)
        return 2

    from simscale_sdk_v1 import SimScaleSDK

    with SimScaleSDK() as sdk:
        result = sdk.network_check()

    _print_human(result)
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
