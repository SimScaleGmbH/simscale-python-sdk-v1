from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class Projects:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def copy_project(
        self,
        project_id: str,
        body: models.ProjectCopyRequest,
    ) -> models.Project:
        """Copy an existing project"""
        return self._client.request(
            "POST",
            f"/projects/{project_id}/copy",
            json_body=body,
            response_type=models.Project,
        )

    def create_project(
        self,
        body: models.Project,
    ) -> models.Project:
        """Create a new project



        The visibility of the Project will be determined by the available capabilities of the requesting user.

        If the user can create private projects, the Project will be private. Otherwise, it will be public.
        """
        return self._client.request(
            "POST",
            "/projects",
            json_body=body,
            response_type=models.Project,
        )

    def get_project(
        self,
        project_id: str,
    ) -> models.Project:
        """Get information about an existing project"""
        return self._client.request(
            "GET",
            f"/projects/{project_id}",
            response_type=models.Project,
        )

    def get_projects(
        self,
        *,
        limit: int | None = None,
        page: int | None = None,
    ) -> PaginatedResponse[models.Project]:
        """List projects"""
        data = self._client.request(
            "GET",
            "/projects",
            query_params={"limit": limit, "page": page},
        )
        return PaginatedResponse(data, models.Project)

    def update_project(
        self,
        project_id: str,
        body: models.Project,
    ) -> None:
        """Update an existing project"""
        return self._client.request(
            "PUT",
            f"/projects/{project_id}",
            json_body=body,
        )
