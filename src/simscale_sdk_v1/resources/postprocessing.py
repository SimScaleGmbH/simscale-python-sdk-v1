from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Postprocessing:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_automatic_states(
        self,
        project_id: str,
        result_id: str,
    ) -> list[models.postprocessing.StateResponse]:
        return self._client.request(
            "GET",
            f"/projects/{project_id}/postprocessing/results/{result_id}/automatic-postprocessor-states",
            response_type=list[models.postprocessing.StateResponse],
        )

    def get_manual_states(
        self,
        project_id: str,
        result_id: str,
    ) -> list[models.postprocessing.StateResponse]:
        return self._client.request(
            "GET",
            f"/projects/{project_id}/postprocessing/results/{result_id}/manual-postprocessor-states",
            response_type=list[models.postprocessing.StateResponse],
        )
