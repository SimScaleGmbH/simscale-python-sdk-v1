from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflow_runner.operation_run_state_history_item import OperationRunStateHistoryItem
from simscale_sdk_v1.models.workflow_runner.operation_run_state_history_statistical_summary import (
    OperationRunStateHistoryStatisticalSummary,
)


class OperationRun(SimScaleModel):
    """Operation level information about workflow run."""

    method_reference: str | None = Field(
        validation_alias="methodReference",
        serialization_alias="methodReference",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
    )
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
    nested_workflow_type_reference: str | None = Field(
        validation_alias="nestedWorkflowTypeReference",
        serialization_alias="nestedWorkflowTypeReference",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
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
    operation_run_state_history: list[OperationRunStateHistoryItem] | None = Field(
        validation_alias="operationRunStateHistory", serialization_alias="operationRunStateHistory", default=None
    )
    operation_type: Literal["METHOD", "NESTED_WORKFLOW", "INLINE"] | None = Field(
        validation_alias="operationType",
        serialization_alias="operationType",
        default=None,
        description="Possible types of an operation run in the workflow run.",
    )
    parameter_values: dict[str, Any] | None = Field(
        validation_alias="parameterValues", serialization_alias="parameterValues", default=None
    )
    recycled: bool | None = Field(default=None)
    state_history_statistical_summary: OperationRunStateHistoryStatisticalSummary | None = Field(
        validation_alias="stateHistoryStatisticalSummary",
        serialization_alias="stateHistoryStatisticalSummary",
        default=None,
    )
    workflow_run_id: str | None = Field(
        validation_alias="workflowRunId",
        serialization_alias="workflowRunId",
        default=None,
        description="Workflow run identifier. It is a string composed of the type identifier and a UUID: `workflow.run:[UUID]`.",
    )
