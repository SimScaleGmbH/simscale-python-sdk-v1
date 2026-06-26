from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class WorkflowRepository:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def create_workflow(
        self,
        body: models.workflow_repository.CreateWorkflowRequest,
    ) -> models.WorkflowId:
        """Create a new workflow with its initial version."""
        return self._client.request(
            "POST",
            "/workflow-repository/workflows",
            json_body=body,
            response_type=models.WorkflowId,
        )

    def list_workflow_versions(
        self,
        workflow_id: str,
        *,
        page: int | None = None,
        size: int | None = None,
        sort_by: str | None = None,
    ) -> list[models.workflow_repository.WorkflowVersionOverview]:
        """List the versions of a workflow."""
        return self._client.request(
            "GET",
            f"/workflow-repository/workflows/{workflow_id}/versions",
            query_params={"page": page, "size": size, "sortBy": sort_by},
            response_type=list[models.workflow_repository.WorkflowVersionOverview],
        )

    def list_workflows(
        self,
        project_id: str,
        *,
        page: int | None = None,
        size: int | None = None,
        sort_by: str | None = None,
    ) -> list[models.workflow_repository.WorkflowOverview]:
        """List workflows in a project."""
        return self._client.request(
            "GET",
            f"/workflow-repository/projects/{project_id}/workflows",
            query_params={"page": page, "size": size, "sortBy": sort_by},
            response_type=list[models.workflow_repository.WorkflowOverview],
        )

    def read_workflow(
        self,
        workflow_id: str,
    ) -> models.workflow_repository.ReadWorkflowResponse:
        """Read a workflow at its latest version."""
        return self._client.request(
            "GET",
            f"/workflow-repository/workflows/{workflow_id}",
            response_type=models.workflow_repository.ReadWorkflowResponse,
        )

    def read_workflow_version(
        self,
        workflow_version_id: str,
        *,
        populate_default_values: bool | None = None,
    ) -> models.workflow_repository.ReadWorkflowResponse:
        """Read a specific workflow version."""
        return self._client.request(
            "GET",
            f"/workflow-repository/workflow-versions/{workflow_version_id}",
            query_params={"populateDefaultValues": populate_default_values},
            response_type=models.workflow_repository.ReadWorkflowResponse,
        )

    def update_workflow(
        self,
        workflow_version_id: str,
        body: models.workflow_repository.UpdateWorkflowRequest,
    ) -> models.WorkflowVersionId:
        """Update a workflow by creating a new version."""
        return self._client.request(
            "POST",
            f"/workflow-repository/workflow-versions/{workflow_version_id}",
            json_body=body,
            response_type=models.WorkflowVersionId,
        )
