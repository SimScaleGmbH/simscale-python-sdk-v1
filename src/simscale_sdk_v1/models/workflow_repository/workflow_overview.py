from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WorkflowOverview(SimScaleModel):
    """Workflow overview data structure. Holds high-level information but skips details (for example data mapping and configuration) to keep the response size reasonably small."""

    created_by: int | None = Field(validation_alias="createdBy", serialization_alias="createdBy", default=None)
    creation_timestamp: datetime | None = Field(
        validation_alias="creationTimestamp", serialization_alias="creationTimestamp", default=None
    )
    description: str | None = Field(default=None)
    last_modification_timestamp: datetime | None = Field(
        validation_alias="lastModificationTimestamp", serialization_alias="lastModificationTimestamp", default=None
    )
    name: str | None = Field(default=None)
    parent_workflow_version_id: str | None = Field(
        validation_alias="parentWorkflowVersionId",
        serialization_alias="parentWorkflowVersionId",
        default=None,
        description="Workflow version identifier. It is a string composed of the type identifier and a UUID: `workflow.version:[UUID]`.",
    )
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
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
