from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.breakpoint import Breakpoint


class WorkflowDefinition(SimScaleModel):
    """Simulation workflow definition.  The definition follows the semantics of a workflow, which is a set of connected operations to generate some desired output data from available input data. The workflow developer defines the data and operations and the workflow engine executes the workflow to achieve the declared goal.  Within the entire definition all data and operations are named. This drives the attention towards the semantics and the domain, also helps with communicating the state of the execution. In regard to consistency validation (name duplications etc.), the framework takes care of that."""

    breakpoints: list[Breakpoint] | None = Field(default=None)
    data: list[Any] | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)
    operations: list[Any] | None = Field(default=None)
    workflow_definition_analysis_strategy: Literal["STATIC", "DYNAMIC"] | None = Field(
        validation_alias="workflowDefinitionAnalysisStrategy",
        serialization_alias="workflowDefinitionAnalysisStrategy",
        default=None,
        description="Possible strategies for analysing the workflow definition.",
    )
    workflow_topology: Literal["LINEAR", "ACYCLIC", "GENERAL"] | None = Field(
        validation_alias="workflowTopology",
        serialization_alias="workflowTopology",
        default=None,
        description="Possible workflow topologies.",
    )
