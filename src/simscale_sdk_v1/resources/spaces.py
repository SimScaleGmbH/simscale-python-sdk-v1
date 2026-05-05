from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Spaces:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_space_info(
        self,
        space_id: str,
    ) -> models.Space:
        """Get Space Info



        Get Space metadata, current user permissions, and view Space settings
        """
        return self._client.request(
            "GET",
            f"/spaces/{space_id}",
            response_type=models.Space,
        )

    def get_user_spaces(self) -> models.Spaces:
        """Get User Spaces



        Get Info about the User Personal Space and all the Team Spaces the user has access to.
        """
        return self._client.request(
            "GET",
            "/spaces",
            response_type=models.Spaces,
        )

    def update_space(
        self,
        space_id: str,
        body: models.Space,
    ) -> models.Space:
        """Update Space



        Update Space metadata and settings
        """
        return self._client.request(
            "PUT",
            f"/spaces/{space_id}",
            json_body=body,
            response_type=models.Space,
        )
