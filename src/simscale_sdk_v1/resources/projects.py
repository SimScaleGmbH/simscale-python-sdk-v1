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
        """Copy an existing project



        The copy has the visibility of the source project unless 'visibility' is set.
        """
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



        Set 'visibility' to create a public or a private project. When omitted, users who can create private projects get a private project,

        all others (for example Community accounts) get a public one. Requesting a private project without a plan that allows it fails with 403.
        """
        return self._client.request(
            "POST",
            "/projects",
            json_body=body,
            response_type=models.Project,
        )

    def delete_project(
        self,
        project_id: str,
    ) -> None:
        """Delete an existing project



        The project is moved to the trash together with its CADs, meshes, simulations and runs.

        Running jobs are stopped. A trashed project can be restored from the SimScale workbench for a limited time.
        """
        return self._client.request(
            "DELETE",
            f"/projects/{project_id}",
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
        project_type: str | None = None,
    ) -> PaginatedResponse[models.Project]:
        """List projects"""
        data = self._client.request(
            "GET",
            "/projects",
            query_params={"limit": limit, "page": page, "projectType": project_type},
        )
        return PaginatedResponse(data, models.Project)

    def update_project(
        self,
        project_id: str,
        body: models.Project,
    ) -> None:
        """Update an existing project



        Set 'visibility' to change between public and private. When omitted, the visibility is kept.
        """
        return self._client.request(
            "PUT",
            f"/projects/{project_id}",
            json_body=body,
        )
