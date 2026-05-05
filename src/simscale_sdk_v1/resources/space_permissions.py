from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class SpacePermissions:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_requester_space_permissions(
        self,
        space_id: str,
    ) -> models.SpacePermissions:
        """Get User Space Permissions



        Get Info about the Permissions that the current requester user has in this Space.
        """
        return self._client.request(
            "GET",
            f"/permissions/spaces/{space_id}/requester",
            response_type=models.SpacePermissions,
        )

    def list_space_permissions(
        self,
        space_id: str,
    ) -> models.Permissions:
        """List Space Permissions



        See who has access to a Space
        """
        return self._client.request(
            "GET",
            f"/permissions/spaces/{space_id}",
            response_type=models.Permissions,
        )

    def update_space_permissions(
        self,
        space_id: str,
        body: models.Permissions,
    ) -> models.Permissions:
        """Update Space Permissions



        Update who has access to a Space.
        """
        return self._client.request(
            "PUT",
            f"/permissions/spaces/{space_id}",
            json_body=body,
            response_type=models.Permissions,
        )
