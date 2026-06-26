from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.breakpoint import Breakpoint


class CreateWorkflowRequest(SimScaleModel):
    """Workflow creation data structure. Holds all properties that one can provide upon creation. Properties which are not presented will not be initialized in the workflow."""

    breakpoints: list[Breakpoint] | None = Field(default=None)
    configuration: Any | None = Field(default=None)
    description: str | None = Field(default=None)
    input_data_map: Any | None = Field(
        validation_alias="inputDataMap", serialization_alias="inputDataMap", default=None
    )
    name: str | None = Field(default=None)
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
    workflow_type_reference: str | None = Field(
        validation_alias="workflowTypeReference",
        serialization_alias="workflowTypeReference",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
    )
