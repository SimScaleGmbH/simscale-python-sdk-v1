from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RecycledOperationRunReference(SimScaleModel):
    """Reference to the earlier operation run whose results a recycled operation run reuses: the workflow run and operation that originally produced them, and the execution behind it."""

    method_run_id: str | None = Field(
        validation_alias="methodRunId",
        serialization_alias="methodRunId",
        default=None,
        description="Method run identifier. It is a string composed of the type identifier and a UUID: `method.run:[UUID]`.",
    )
    nested_workflow_run_id: str | None = Field(
        validation_alias="nestedWorkflowRunId",
        serialization_alias="nestedWorkflowRunId",
        default=None,
        description="Workflow run identifier. It is a string composed of the type identifier and a UUID: `workflow.run:[UUID]`.",
    )
    operation_name: str | None = Field(
        validation_alias="operationName", serialization_alias="operationName", default=None
    )
    operation_run_id: str | None = Field(
        validation_alias="operationRunId",
        serialization_alias="operationRunId",
        default=None,
        description="Operation run identifier. It is a string composed of the type identifier and a UUID: `operation.run:[UUID]`.",
    )
    workflow_run_id: str | None = Field(
        validation_alias="workflowRunId",
        serialization_alias="workflowRunId",
        default=None,
        description="Workflow run identifier. It is a string composed of the type identifier and a UUID: `workflow.run:[UUID]`.",
    )
