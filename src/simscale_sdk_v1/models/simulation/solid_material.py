from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__density import DimensionalFunction_Density
from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat
from simscale_sdk_v1.models.simulation.isotropic_expansion import IsotropicExpansion
from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
from simscale_sdk_v1.models.simulation.one_of__solid_material_conductivity import OneOf_SolidMaterialConductivity
from simscale_sdk_v1.models.simulation.one_of__solid_material_material_behavior import (
    OneOf_SolidMaterialMaterialBehavior,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SolidMaterial(SimScaleModel):
    name: str | None = Field(default=None)
    material_behavior: OneOf_SolidMaterialMaterialBehavior | None = Field(
        validation_alias="materialBehavior", serialization_alias="materialBehavior", default=None
    )
    density: DimensionalFunction_Density | None = Field(default=None)
    expansion: IsotropicExpansion | None = Field(default=None)
    conductivity: OneOf_SolidMaterialConductivity | None = Field(default=None)
    specific_heat: DimensionalFunction_SpecificHeat | None = Field(
        validation_alias="specificHeat", serialization_alias="specificHeat", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    built_in_material: str | None = Field(
        validation_alias="builtInMaterial", serialization_alias="builtInMaterial", default=None
    )
    material_library_reference: MaterialLibraryReference | None = Field(
        validation_alias="materialLibraryReference", serialization_alias="materialLibraryReference", default=None
    )
