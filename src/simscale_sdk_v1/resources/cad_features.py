from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class CadFeatures:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def add_cad_feature(
        self,
        cad_id: str,
        cad_state_id: str,
        body: models.cad.CadFeatureRequest,
    ) -> models.CadFeatureResponse:
        """Add a feature to the CAD



        Adding a CAD feature that involves complex computation might take some time to complete.

        Please refer to the following steps to start a CAD feature generation and check its progress:

        1. Trigger the CAD feature generation via `POST /cads/{cadId}/states/{cadStateId}/features`

        2. Monitor progress via `GET /cads/{cadId}/features/progress`
        """
        return self._client.request(
            "POST",
            f"/cads/{cad_id}/states/{cad_state_id}/features",
            json_body=body,
            response_type=models.CadFeatureResponse,
        )

    def get_cad_feature_event_log(
        self,
        cad_id: str,
        cad_state_id: str,
        cad_feature_id: str,
    ) -> models.EventLogResponse:
        """Get the CAD feature event log"""
        return self._client.request(
            "GET",
            f"/cads/{cad_id}/states/{cad_state_id}/features/{cad_feature_id}/eventlog",
            response_type=models.EventLogResponse,
        )

    def get_cad_features_progress(
        self,
        cad_id: str,
    ) -> models.CadFeatureResponse:
        """Monitor CAD feature generation progress



        Monitor CAD feature generation progress for long-running processes.
        """
        return self._client.request(
            "GET",
            f"/cads/{cad_id}/features/progress",
            response_type=models.CadFeatureResponse,
        )
