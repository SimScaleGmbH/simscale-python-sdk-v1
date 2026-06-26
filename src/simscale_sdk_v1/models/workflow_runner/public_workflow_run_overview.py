from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PublicWorkflowRunOverview(SimScaleModel):
    """Public-API overview of a workflow run. When the run is in the SUCCEEDED state, `outputDataMap` is populated with the DataIds of the run's outputs; in all other states (including in listings) the field is null."""

    creation_timestamp: datetime | None = Field(
        validation_alias="creationTimestamp", serialization_alias="creationTimestamp", default=None
    )
    error: Any | None = Field(default=None)
    has_recycled_operation: bool | None = Field(
        validation_alias="hasRecycledOperation", serialization_alias="hasRecycledOperation", default=None
    )
    last_processed: datetime | None = Field(
        validation_alias="lastProcessed", serialization_alias="lastProcessed", default=None
    )
    output_data_map: Any | None = Field(
        validation_alias="outputDataMap", serialization_alias="outputDataMap", default=None
    )
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
    state: Literal["CREATED", "RUNNING", "PAUSED", "CANCELING", "SUCCEEDED", "FAILED", "CANCELED"] | None = Field(
        default=None, description="Workflow run state is a higher-level state describing overall progression."
    )
    workflow_id: str | None = Field(
        validation_alias="workflowId",
        serialization_alias="workflowId",
        default=None,
        description="Workflow identifier. It is a string composed of the type identifier and a UUID: `workflow:[UUID]`.",
    )
    workflow_run_id: str | None = Field(
        validation_alias="workflowRunId",
        serialization_alias="workflowRunId",
        default=None,
        description="Workflow run identifier. It is a string composed of the type identifier and a UUID: `workflow.run:[UUID]`.",
    )
    workflow_run_mode: Literal["DRY", "REAL"] | None = Field(
        validation_alias="workflowRunMode", serialization_alias="workflowRunMode", default=None
    )
    workflow_run_name: str | None = Field(
        validation_alias="workflowRunName", serialization_alias="workflowRunName", default=None
    )
    workflow_type_reference: str | None = Field(
        validation_alias="workflowTypeReference",
        serialization_alias="workflowTypeReference",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
    )
    workflow_version_id: str | None = Field(
        validation_alias="workflowVersionId",
        serialization_alias="workflowVersionId",
        default=None,
        description="Workflow version identifier. It is a string composed of the type identifier and a UUID: `workflow.version:[UUID]`.",
    )
