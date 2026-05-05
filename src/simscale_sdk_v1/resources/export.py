from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Export:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_export(
        self,
        project_id: str,
        body: models.CreateExportRequest,
    ) -> models.CreateExportResponse:
        """Trigger an export for a simulation result"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/export",
            json_body=body,
            response_type=models.CreateExportResponse,
        )

    def get_export(
        self,
        project_id: str,
        export_id: str,
    ) -> models.GetExportResponse:
        """Get the status of the export and temporary download link to the exported object if it is done"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/export/{export_id}",
            response_type=models.GetExportResponse,
        )
