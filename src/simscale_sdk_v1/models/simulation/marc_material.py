from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__density import DimensionalFunction_Density
from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
from simscale_sdk_v1.models.simulation.one_of__marc_material_marc_material_behavior import (
    OneOf_MarcMaterialMarcMaterialBehavior,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MarcMaterial(SimScaleModel):
    name: str | None = Field(default=None)
    marc_material_behavior: OneOf_MarcMaterialMarcMaterialBehavior | None = Field(
        validation_alias="marcMaterialBehavior", serialization_alias="marcMaterialBehavior", default=None
    )
    density: DimensionalFunction_Density | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    built_in_material: str | None = Field(
        validation_alias="builtInMaterial", serialization_alias="builtInMaterial", default=None
    )
    material_library_reference: MaterialLibraryReference | None = Field(
        validation_alias="materialLibraryReference", serialization_alias="materialLibraryReference", default=None
    )
