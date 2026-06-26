from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflow_runner.operation_run_progress import OperationRunProgress


class WorkflowRunProgress(SimScaleModel):
    """Represents the progress of a workflow run"""

    elapsed_time_in_seconds: int | None = Field(
        validation_alias="elapsedTimeInSeconds", serialization_alias="elapsedTimeInSeconds", default=None
    )
    estimated_remaining_time_in_seconds: int | None = Field(
        validation_alias="estimatedRemainingTimeInSeconds",
        serialization_alias="estimatedRemainingTimeInSeconds",
        default=None,
    )
    finished: list[OperationRunProgress] | None = Field(default=None)
    pending: list[OperationRunProgress] | None = Field(default=None)
    percentage: float | None = Field(default=None)
    running: list[OperationRunProgress] | None = Field(default=None)
    skipped: list[OperationRunProgress] | None = Field(default=None)
    workflow_run_id: str | None = Field(
        validation_alias="workflowRunId",
        serialization_alias="workflowRunId",
        default=None,
        description="Workflow run identifier. It is a string composed of the type identifier and a UUID: `workflow.run:[UUID]`.",
    )
