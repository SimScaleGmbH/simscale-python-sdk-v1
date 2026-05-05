from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class TableImports:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def import_table(
        self,
        project_id: str,
        body: models.TableImportRequest,
    ) -> models.TableImportResponse:
        """Import a new table for reference within a Simulation spec



        Table import requires the following steps:

        1. Request a temporary storage location via `POST /storage`.

        2. Upload your table definition using the HTTP `PUT` method to the `url` provided in the temporary storage location response object.

        3. Import via `POST /projects/{projectId}/tableimports` and include the `storageId` provided in the temporary storage location response object.
        """
        return self._client.request(
            "POST",
            f"/projects/{project_id}/tableimports",
            json_body=body,
            response_type=models.TableImportResponse,
        )
