from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.breakpoint import Breakpoint


class ReadWorkflowResponse(SimScaleModel):
    """Workflow or workflow version reading response. Contains all properties available for the requested workflow or workflow version."""

    breakpoints: list[Breakpoint] | None = Field(default=None)
    configuration: Any | None = Field(default=None)
    created_by: int | None = Field(validation_alias="createdBy", serialization_alias="createdBy", default=None)
    description: str | None = Field(default=None)
    input_data_map: Any | None = Field(
        validation_alias="inputDataMap", serialization_alias="inputDataMap", default=None
    )
    name: str | None = Field(default=None)
    origin: Literal["CREATED", "UPDATED", "MIGRATED", "COPIED"] | None = Field(
        default=None, description="The operation through which the workflow version came into existence."
    )
    parent_workflow_version_id: str | None = Field(
        validation_alias="parentWorkflowVersionId",
        serialization_alias="parentWorkflowVersionId",
        default=None,
        description="Workflow version identifier. It is a string composed of the type identifier and a UUID: `workflow.version:[UUID]`.",
    )
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
    timestamp: datetime | None = Field(default=None)
    workflow_id: str | None = Field(
        validation_alias="workflowId",
        serialization_alias="workflowId",
        default=None,
        description="Workflow identifier. It is a string composed of the type identifier and a UUID: `workflow:[UUID]`.",
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
