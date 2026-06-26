"""Helper methods mixed into SimScaleSDK."""

from __future__ import annotations

import time
import uuid
from collections.abc import Iterator, Mapping
from contextlib import suppress
from pathlib import Path
from typing import TYPE_CHECKING, Any

import httpx

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import SimScaleOperationError

if TYPE_CHECKING:
    from simscale_sdk_v1.models.data_repository import PresignedRequest

_DEFAULT_UPLOAD_SESSION_CHUNK_SIZE = 2_000_000_000
_UPLOAD_BUFFER_SIZE = 8 * 1024 * 1024


class SimScaleHelpers:
    """Mixin providing convenience methods for SimScaleSDK."""

    def wait_until_done(
        self,
        poll_fn,
        *,
        timeout=3600,
        interval=30,
        terminal_statuses=("FINISHED", "SUCCEEDED", "CANCELED", "FAILED", "DONE", "EXPIRED"),
        success_statuses=("FINISHED", "SUCCEEDED", "DONE"),
        raise_on_failure=True,
        get_status=lambda result: result.status,
    ):
        """Poll until status reaches a terminal state.

        Raises SimScaleOperationError if the operation fails (unless raise_on_failure=False).
        Raises TimeoutError if timeout is exceeded.
        """
        start = time.monotonic()
        result = poll_fn()
        status = get_status(result)
        while status not in terminal_statuses:
            if time.monotonic() - start > timeout:
                raise TimeoutError(f"Timed out after {timeout}s (last status: {status})")
            time.sleep(interval)
            result = poll_fn()
            status = get_status(result)
        if raise_on_failure and status not in success_statuses:
            raise SimScaleOperationError(result)
        return result

    def get_material(self, name: str, *, group: str | None = None) -> models.MaterialResponse:
        """Look up a material by name. Uses the SimScale default library unless group is specified."""
        groups = self.materials.get_material_groups(limit=100).embedded
        if group:
            material_group = next((g for g in groups if g.name == group), None)
            if not material_group:
                available = [g.name for g in groups]
                raise ValueError(f"Material group '{group}' not found. Available: {available}")
        else:
            material_group = next(
                (g for g in groups if g.group_type == "SIMSCALE_DEFAULT"),
                None,
            )
            if not material_group:
                raise ValueError("Could not find the SimScale default material group")
        materials = self.materials.get_materials(material_group_id=material_group.material_group_id, limit=100).embedded
        material = next((m for m in materials if m.name == name), None)
        if not material:
            available = [m.name for m in materials]
            raise ValueError(f"Material '{name}' not found. Available: {available}")
        return self.materials.get_material_data(
            material_group_id=material_group.material_group_id,
            material_id=material.id,
        )

    def upload(self, filepath: str | Path) -> models.Storage:
        """Create a storage entry and upload a file. Returns the Storage object (use .storage_id)."""
        storage = self.storage.create_storage()
        self._client.upload_to_storage(storage.url, filepath)
        return storage

    def download(self, url: str, filepath: str | Path) -> None:
        """Download a file from a URL to a local path."""
        self._client.download(url, filepath)

    def upload_to_data_repository(
        self,
        filepath: str | Path,
        *,
        project_id: str,
        data_type: str,
        content_type: str = "application/octet-stream",
        chunk_size: int = _DEFAULT_UPLOAD_SESSION_CHUNK_SIZE,
    ) -> models.DataId:
        """Upload a file to data-repository and return its DataId.

        The file is split into sequential append operations. Each chunk is
        uploaded directly to the pre-signed URL returned by the API, then
        finished before the next append starts. The default chunk size is
        2,000,000,000 bytes (2 GB), matching the direct upload limit.
        """
        path = Path(filepath)
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")

        file_size = path.stat().st_size
        if file_size == 0:
            raise ValueError("upload sessions require a non-empty file")

        upload_session = self.data_repository.create_upload_session(
            models.data_repository.CreateUploadSessionRequest(
                data_type=data_type,
                content_type=content_type,
            ),
            project_id=project_id,
        )
        storage_id = upload_session.storage_id
        if storage_id is None:
            raise RuntimeError("Upload session response did not contain storage_id")

        try:
            offset = 0
            while offset < file_size:
                current_chunk_size = min(chunk_size, file_size - offset)
                append = self.data_repository.start_upload_session_append(
                    storage_id,
                    models.data_repository.StartUploadSessionAppendRequest(size=current_chunk_size),
                    project_id=project_id,
                )
                append_id = append.append_id
                if append_id is None:
                    raise RuntimeError("Upload session append response did not contain append_id")

                try:
                    self._upload_file_range_to_presigned_request(
                        append.pre_signed_put_request,
                        path,
                        offset=offset,
                        size=current_chunk_size,
                    )
                    self.data_repository.finish_upload_session_append(storage_id, append_id, project_id=project_id)
                except Exception:
                    with suppress(Exception):
                        self.data_repository.cancel_upload_session_append(storage_id, append_id, project_id=project_id)
                    raise

                offset += current_chunk_size

            return self.data_repository.finalize_upload_session(storage_id, project_id=project_id)
        except Exception:
            with suppress(Exception):
                self.data_repository.delete_upload_session(storage_id, project_id=project_id)
            raise

    def create_non_parametric_workflow_data_map(self, data_by_name: Mapping[str, str]) -> dict[str, Any]:
        """Create a workflow data map for workflows without parameter values.

        Workflow data maps support parameter-value combinations. For non-parametric
        data there is one combination with empty parameter values; its UUID only
        links both sections of this serialized data map.
        """
        parameter_value_combination_id = str(uuid.uuid4())
        return {
            "parameterValueCombinationsById": {
                parameter_value_combination_id: {
                    "parameterValues": {},
                },
            },
            "dataByNameAndParameterValueCombinationId": {
                name: {
                    parameter_value_combination_id: data_id,
                }
                for name, data_id in data_by_name.items()
            },
        }

    def get_non_parametric_workflow_data_id(self, data_map: Mapping[str, Any], data_name: str) -> str | None:
        """Read a data ID from a workflow data map without parameter values."""
        data_by_parameter_id = data_map.get("dataByNameAndParameterValueCombinationId", {}).get(data_name, {})
        return next(iter(data_by_parameter_id.values()), None)

    def close(self) -> None:
        self._client.close()

    def _upload_file_range_to_presigned_request(
        self,
        presigned_request: PresignedRequest | None,
        path: Path,
        *,
        offset: int,
        size: int,
    ) -> None:
        if presigned_request is None or presigned_request.url is None:
            raise RuntimeError("Upload session append response did not contain a pre-signed PUT URL")

        headers = {
            header.name: header.value
            for header in presigned_request.headers or []
            if header.name is not None and header.value is not None
        }
        headers.setdefault("Content-Length", str(size))

        with path.open("rb") as file:
            file.seek(offset)
            response = httpx.put(
                presigned_request.url,
                content=self._read_file_range(file, size),
                headers=headers,
                timeout=httpx.Timeout(3600.0, connect=30.0),
                follow_redirects=True,
            )

        if not (200 <= response.status_code < 300):
            from simscale_sdk_v1.client import SimScaleAPIError

            raise SimScaleAPIError(response.status_code, response.text, response)

    @staticmethod
    def _read_file_range(file, size: int) -> Iterator[bytes]:
        remaining = size
        while remaining > 0:
            chunk = file.read(min(_UPLOAD_BUFFER_SIZE, remaining))
            if not chunk:
                raise OSError(f"Unexpected end of file with {remaining} bytes left to upload")
            remaining -= len(chunk)
            yield chunk

    def __enter__(self):
        return self

    def __exit__(self, *args) -> None:
        self.close()
