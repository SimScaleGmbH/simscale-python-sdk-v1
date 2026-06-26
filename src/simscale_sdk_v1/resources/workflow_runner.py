from __future__ import annotations

from simscale_sdk_v1 import models
from simscale_sdk_v1.client import PaginatedResponse, SimScaleClient


class WorkflowRunner:
    def __init__(self, client: SimScaleClient) -> None:
        self._client = client

    def cancel_workflow_run(
        self,
        workflow_run_id: str,
    ) -> None:
        """Cancel a workflow run."""
        return self._client.request(
            "POST",
            f"/workflow-runner/runs/{workflow_run_id}/cancel",
        )

    def get_method_run_resource_usage_report(
        self,
        method_run_id: str,
    ) -> models.workflow_runner.MethodResourceUsageReport:
        """Read a method run's resource-usage report."""
        return self._client.request(
            "GET",
            f"/workflow-runner/method-runs/{method_run_id}/resource-usage",
            response_type=models.workflow_runner.MethodResourceUsageReport,
        )

    def get_operation_run(
        self,
        operation_run_id: str,
    ) -> models.workflow_runner.OperationRun:
        """Read an operation run."""
        return self._client.request(
            "GET",
            f"/workflow-runner/operation-runs/{operation_run_id}",
            response_type=models.workflow_runner.OperationRun,
        )

    def get_workflow_run(
        self,
        workflow_run_id: str,
    ) -> models.workflow_runner.PublicWorkflowRunOverview:
        """Read a workflow run."""
        return self._client.request(
            "GET",
            f"/workflow-runner/runs/{workflow_run_id}",
            response_type=models.workflow_runner.PublicWorkflowRunOverview,
        )

    def get_workflow_run_progress(
        self,
        workflow_run_id: str,
    ) -> models.workflow_runner.WorkflowRunProgress:
        """Read the progress of a workflow run."""
        return self._client.request(
            "GET",
            f"/workflow-runner/runs/{workflow_run_id}/progress",
            response_type=models.workflow_runner.WorkflowRunProgress,
        )

    def initialize_workflow_run(
        self,
        body: models.workflow_runner.InitializeWorkflowRunRequest,
    ) -> models.WorkflowRunId:
        """Initialize a workflow run from a workflow version."""
        return self._client.request(
            "POST",
            "/workflow-runner/runs",
            json_body=body,
            response_type=models.WorkflowRunId,
        )

    def list_workflow_runs_by_workflow(
        self,
        workflow_id: str,
        *,
        page: int | None = None,
        size: int | None = None,
        sort_by: str | None = None,
    ) -> list[models.workflow_runner.PublicWorkflowRunOverview]:
        """List the workflow runs of a workflow."""
        return self._client.request(
            "GET",
            f"/workflow-runner/workflows/{workflow_id}/runs",
            query_params={"page": page, "size": size, "sortBy": sort_by},
            response_type=list[models.workflow_runner.PublicWorkflowRunOverview],
        )

    def pause_workflow_run(
        self,
        workflow_run_id: str,
    ) -> None:
        """Pause a running workflow run."""
        return self._client.request(
            "POST",
            f"/workflow-runner/runs/{workflow_run_id}/pause",
        )

    def resume_workflow_run(
        self,
        workflow_run_id: str,
    ) -> None:
        """Resume a paused workflow run."""
        return self._client.request(
            "POST",
            f"/workflow-runner/runs/{workflow_run_id}/resume",
        )

    def start_workflow_run(
        self,
        workflow_run_id: str,
    ) -> None:
        """Start a workflow run."""
        return self._client.request(
            "POST",
            f"/workflow-runner/runs/{workflow_run_id}/start",
        )
