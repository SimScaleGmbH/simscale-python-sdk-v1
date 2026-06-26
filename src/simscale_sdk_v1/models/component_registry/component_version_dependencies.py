from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ComponentVersionDependencies(SimScaleModel):
    """Contains the dependencies of a component version, grouped by component type. Note that not all component types can have dependencies of all component types. For instance, data types can only depend on other data types, but not methods or workflows."""

    data_type_dependencies: list[str] | None = Field(
        validation_alias="dataTypeDependencies", serialization_alias="dataTypeDependencies", default=None
    )
    engineering_ai_agent_dependencies: list[str] | None = Field(
        validation_alias="engineeringAiAgentDependencies",
        serialization_alias="engineeringAiAgentDependencies",
        default=None,
    )
    method_dependencies: list[str] | None = Field(
        validation_alias="methodDependencies", serialization_alias="methodDependencies", default=None
    )
    physics_ai_model_dependencies: list[str] | None = Field(
        validation_alias="physicsAiModelDependencies", serialization_alias="physicsAiModelDependencies", default=None
    )
    workflow_type_dependencies: list[str] | None = Field(
        validation_alias="workflowTypeDependencies", serialization_alias="workflowTypeDependencies", default=None
    )
