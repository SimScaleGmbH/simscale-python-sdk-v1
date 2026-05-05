from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Storage:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_storage(self) -> models.Storage:
        """Create a temporary storage location"""
        return self._client.request(
            "POST",
            "/storage",
            response_type=models.Storage,
        )
