from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.element_technology_definition import ElementTechnologyDefinition


class CustomElementDefinitionMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomElementDefinitionMethod",
    )
    mechanical_mesh_element_order: Literal["FIRST", "SECOND"] | None = Field(
        validation_alias="mechanicalMeshElementOrder", serialization_alias="mechanicalMeshElementOrder", default=None
    )
    thermal_mesh_element_order: Literal["FIRST", "SECOND"] | None = Field(
        validation_alias="thermalMeshElementOrder", serialization_alias="thermalMeshElementOrder", default="FIRST"
    )
    reduced_integration: bool | None = Field(
        validation_alias="reducedIntegration", serialization_alias="reducedIntegration", default=False
    )
    lumped_mass: bool | None = Field(validation_alias="lumpedMass", serialization_alias="lumpedMass", default=False)
    definitions: list[ElementTechnologyDefinition] | None = Field(default=None)
