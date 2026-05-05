from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class CadImports:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_cad_import_event_log(
        self,
        project_id: str,
        cad_id: str,
    ) -> models.EventLogResponse:
        """Get the CAD import event log"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/cadimports/{cad_id}/eventlog",
            response_type=models.EventLogResponse,
        )

    def get_imported_cad(
        self,
        project_id: str,
        cad_id: str,
    ) -> models.CadImportResponse:
        """Get information about the imported CAD"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}/cadimports/{cad_id}",
            response_type=models.CadImportResponse,
        )

    def import_cad(
        self,
        project_id: str,
        body: models.CadImportRequest,
    ) -> models.CadImportResponse:
        """Import a new CAD from file



        CAD import requires the following steps:

        1. Request a temporary storage location via `POST /storage`.

        2. Upload your CAD file using the HTTP `PUT` method to the `url` provided in the temporary storage location response object.

        3. Start the import via `POST /projects/{projectId}/cadimports` and include the `storageId` provided in the temporary storage location response object.

        4. Check for the import status via `GET /projects/{projectId}/cadimports/{cadId}`.
        """
        return self._client.request(
            "POST",
            f"/projects/{project_id}/cadimports",
            json_body=body,
            response_type=models.CadImportResponse,
        )
