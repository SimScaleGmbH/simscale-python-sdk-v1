from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.material_library_reference import MaterialLibraryReference
from simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_electric_conductivity_type import (
    OneOf_SolidCompressibleMaterialElectricConductivityType,
)
from simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_radiative_behavior import (
    OneOf_SolidCompressibleMaterialRadiativeBehavior,
)
from simscale_sdk_v1.models.simulation.one_of__solid_compressible_material_transport import (
    OneOf_SolidCompressibleMaterialTransport,
)
from simscale_sdk_v1.models.simulation.specie_default import SpecieDefault
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SolidCompressibleMaterial(SimScaleModel):
    name: str | None = Field(default=None)
    specie: SpecieDefault | None = Field(default=None)
    transport: OneOf_SolidCompressibleMaterialTransport | None = Field(default=None)
    emissivity: float | None = Field(default=0.9)
    radiative_behavior: OneOf_SolidCompressibleMaterialRadiativeBehavior | None = Field(
        validation_alias="radiativeBehavior", serialization_alias="radiativeBehavior", default=None
    )
    electric_conductivity_type: OneOf_SolidCompressibleMaterialElectricConductivityType | None = Field(
        validation_alias="electricConductivityType", serialization_alias="electricConductivityType", default=None
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
