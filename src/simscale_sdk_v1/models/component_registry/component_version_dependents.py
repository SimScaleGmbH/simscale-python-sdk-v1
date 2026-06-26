from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ComponentVersionDependents(SimScaleModel):
    """Contains the component versions dependent on a component version, grouped by component type. Note that not all component types can have dependents of all component types. For instance, data types cannot depend on methods or workflow types."""

    data_type_dependents: list[str] | None = Field(
        validation_alias="dataTypeDependents", serialization_alias="dataTypeDependents", default=None
    )
    engineering_ai_agent_dependents: list[str] | None = Field(
        validation_alias="engineeringAiAgentDependents",
        serialization_alias="engineeringAiAgentDependents",
        default=None,
    )
    method_dependents: list[str] | None = Field(
        validation_alias="methodDependents", serialization_alias="methodDependents", default=None
    )
    physics_ai_model_dependents: list[str] | None = Field(
        validation_alias="physicsAiModelDependents", serialization_alias="physicsAiModelDependents", default=None
    )
    workflow_type_dependents: list[str] | None = Field(
        validation_alias="workflowTypeDependents", serialization_alias="workflowTypeDependents", default=None
    )
