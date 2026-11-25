from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient, path_segment


class ProjectPermissions:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def get_requester_project_permissions(
        self,
        project_id: str,
    ) -> models.ProjectPermissions:
        """Get User Project Permissions



        Get Info about the Permissions that the current requester user has for this Project.
        """
        return self._client.request(
            "GET",
            f"/permissions/projects/{path_segment(project_id)}/requester",
            response_type=models.ProjectPermissions,
        )
