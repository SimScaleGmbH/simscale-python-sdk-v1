from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflow_runner.method_progress_entry import MethodProgressEntry


class OperationRunProgress(SimScaleModel):
    """Details about an individual operation run's progress."""

    elapsed_time_in_seconds: int | None = Field(
        validation_alias="elapsedTimeInSeconds", serialization_alias="elapsedTimeInSeconds", default=None
    )
    estimated_remaining_time_in_seconds: int | None = Field(
        validation_alias="estimatedRemainingTimeInSeconds",
        serialization_alias="estimatedRemainingTimeInSeconds",
        default=None,
    )
    method_progress: list[MethodProgressEntry] | None = Field(
        validation_alias="methodProgress", serialization_alias="methodProgress", default=None
    )
    method_run_id: str | None = Field(
        validation_alias="methodRunId",
        serialization_alias="methodRunId",
        default=None,
        description="Method run identifier. It is a string composed of the type identifier and a UUID: `method.run:[UUID]`.",
    )
    nested_run_progress: Any | None = Field(
        validation_alias="nestedRunProgress", serialization_alias="nestedRunProgress", default=None
    )
    nested_workflow_run_id: str | None = Field(
        validation_alias="nestedWorkflowRunId",
        serialization_alias="nestedWorkflowRunId",
        default=None,
        description="Workflow run identifier. It is a string composed of the type identifier and a UUID: `workflow.run:[UUID]`.",
    )
    operation_label: str | None = Field(
        validation_alias="operationLabel", serialization_alias="operationLabel", default=None
    )
    operation_multi_language_label: dict[str, str] | None = Field(
        validation_alias="operationMultiLanguageLabel", serialization_alias="operationMultiLanguageLabel", default=None
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
    operation_type: Literal["METHOD", "NESTED_WORKFLOW", "INLINE"] | None = Field(
        validation_alias="operationType",
        serialization_alias="operationType",
        default=None,
        description="Possible types of an operation run in the workflow run.",
    )
    percentage: float | None = Field(default=None)
