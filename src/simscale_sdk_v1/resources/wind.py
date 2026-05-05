from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Wind:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_wind_data(
        self,
        *,
        latitude: str | None = None,
        longitude: str | None = None,
    ) -> models.WindRoseResponse:
        """Get wind condition for given coordinates"""
        return self._client.request(
            "GET",
            "/winddata",
            query_params={"latitude": latitude, "longitude": longitude},
            response_type=models.WindRoseResponse,
        )
