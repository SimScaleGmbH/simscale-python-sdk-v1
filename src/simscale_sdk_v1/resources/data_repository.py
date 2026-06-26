from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class DataRepository:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def cancel_upload_session_append(
        self,
        storage_id: str,
        append_id: str,
        *,
        project_id: str | None = None,
    ) -> None:
        """Cancel an append operation."""
        return self._client.request(
            "POST",
            f"/data-repository/data/upload-sessions/{storage_id}/appends/{append_id}/cancel",
            query_params={"projectId": project_id},
        )

    def create_upload_session(
        self,
        body: models.data_repository.CreateUploadSessionRequest,
        *,
        project_id: str | None = None,
    ) -> models.data_repository.UploadSession:
        """Initialize an upload session backed by pre-signed URLs."""
        return self._client.request(
            "POST",
            "/data-repository/data/upload-sessions",
            json_body=body,
            query_params={"projectId": project_id},
            response_type=models.data_repository.UploadSession,
        )

    def delete_upload_session(
        self,
        storage_id: str,
        *,
        project_id: str | None = None,
    ) -> None:
        """Delete an initialized upload session."""
        return self._client.request(
            "DELETE",
            f"/data-repository/data/upload-sessions/{storage_id}",
            query_params={"projectId": project_id},
        )

    def download_data(
        self,
        data_id: str,
        *,
        filename: str | None = None,
    ) -> bytes:
        """Download an existing data object.



        Streams the bytes of an internally-stored data object to the response body.

        The original `Content-Type` recorded at upload time is replayed on the

        response, sanitized against an allowlist for browser safety.
        """
        return self._client.request(
            "GET",
            f"/data-repository/data/{data_id}/content",
            query_params={"filename": filename},
            response_binary=True,
        )

    def finalize_upload_session(
        self,
        storage_id: str,
        *,
        project_id: str | None = None,
    ) -> models.DataId:
        """Finalize an upload session and register it as data."""
        return self._client.request(
            "POST",
            f"/data-repository/data/upload-sessions/{storage_id}/finalize",
            query_params={"projectId": project_id},
            response_type=models.DataId,
        )

    def finish_upload_session_append(
        self,
        storage_id: str,
        append_id: str,
        *,
        project_id: str | None = None,
    ) -> None:
        """Finish an append operation after the chunk was uploaded through its pre-signed URL."""
        return self._client.request(
            "POST",
            f"/data-repository/data/upload-sessions/{storage_id}/appends/{append_id}/finish",
            query_params={"projectId": project_id},
        )

    def get_data_info(
        self,
        data_id: str,
    ) -> models.data_repository.DataInfo:
        """Read the metadata of a data object."""
        return self._client.request(
            "GET",
            f"/data-repository/data/{data_id}",
            response_type=models.data_repository.DataInfo,
        )

    def list_data(
        self,
        project_id: str,
        *,
        origin: str | None = None,
        page: int | None = None,
        size: int | None = None,
        sort_by: str | None = None,
    ) -> list[models.DataId]:
        """List data objects in a project."""
        return self._client.request(
            "GET",
            f"/data-repository/projects/{project_id}/data",
            query_params={"origin": origin, "page": page, "size": size, "sortBy": sort_by},
            response_type=list[models.DataId],
        )

    def start_upload_session_append(
        self,
        storage_id: str,
        body: models.data_repository.StartUploadSessionAppendRequest,
        *,
        project_id: str | None = None,
    ) -> models.data_repository.UploadSessionAppend:
        """Start appending a chunk to an initialized upload session."""
        return self._client.request(
            "POST",
            f"/data-repository/data/upload-sessions/{storage_id}/appends",
            json_body=body,
            query_params={"projectId": project_id},
            response_type=models.data_repository.UploadSessionAppend,
        )

    def upload_data(
        self,
        content: bytes | BinaryIO | Path,
        *,
        data_type: str | None = None,
        project_id: str | None = None,
        content_type: str | None = None,
    ) -> models.DataId:
        """Upload a new data object."""
        return self._client.request(
            "POST",
            "/data-repository/data",
            binary_body=content,
            content_type=content_type,
            query_params={"dataType": data_type, "projectId": project_id},
            response_type=models.DataId,
        )
