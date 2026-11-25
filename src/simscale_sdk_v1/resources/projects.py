from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient, path_segment


class Projects:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def copy_project(
        self,
        project_id: str,
        body: models.ProjectCopyRequest,
    ) -> models.Project:
        """Copy an existing project



        Deprecated: large projects can take longer to copy than the request is allowed to run.

        Start the copy via `POST /projects/{projectId}/copies` and check its status via `GET /projects/{projectId}/copies/{projectCopyId}` instead.



        Unless 'visibility' is set, the copy is private on a Professional plan and has the visibility of the source project otherwise.
        """
        return self._client.request(
            "POST",
            f"/projects/{path_segment(project_id)}/copy",
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
            f"/projects/{path_segment(project_id)}",
        )

    def get_project(
        self,
        project_id: str,
    ) -> models.Project:
        """Get information about an existing project"""
        return self._client.request(
            "GET",
            f"/projects/{path_segment(project_id)}",
            response_type=models.Project,
        )

    def get_project_copy(
        self,
        project_id: str,
        project_copy_id: str,
    ) -> models.ProjectCopyResponse:
        """Get information about the project copy



        Only the user who started the copy can read it. Finished copies can be read for 7 days.
        """
        return self._client.request(
            "GET",
            f"/projects/{path_segment(project_id)}/copies/{path_segment(project_copy_id)}",
            response_type=models.ProjectCopyResponse,
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

    def start_project_copy(
        self,
        project_id: str,
        body: models.ProjectCopyRequest,
    ) -> models.ProjectCopyResponse:
        """Start copying an existing project



        Copying a project requires the following steps:

        1. Start the copy via `POST /projects/{projectId}/copies`.

        2. Check for the copy status via `GET /projects/{projectId}/copies/{projectCopyId}` until it is `FINISHED` or `FAILED`.

        3. Once `FINISHED`, the `projectId` of the response is the ID of the new project.



        Unless 'visibility' is set, the copy is private on a Professional plan and has the visibility of the source project otherwise.
        """
        return self._client.request(
            "POST",
            f"/projects/{path_segment(project_id)}/copies",
            json_body=body,
            response_type=models.ProjectCopyResponse,
        )

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
            f"/projects/{path_segment(project_id)}",
            json_body=body,
        )
