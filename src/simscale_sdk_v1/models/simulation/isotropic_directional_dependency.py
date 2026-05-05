from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_expansion_rate import (
    DimensionalFunction_ThermalExpansionRate,
)
from simscale_sdk_v1.models.simulation.one_of__isotropic_directional_dependency_poissons_ratio import (
    OneOf_IsotropicDirectionalDependencyPoissonsRatio,
)


class IsotropicDirectionalDependency(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Schema name: IsotropicDirectionalDependency",
    )
    youngs_modulus: DimensionalFunction_Pressure | None = Field(
        validation_alias="youngsModulus", serialization_alias="youngsModulus", default=None
    )
    poissons_ratio: OneOf_IsotropicDirectionalDependencyPoissonsRatio | None = Field(
        validation_alias="poissonsRatio", serialization_alias="poissonsRatio", default=None
    )
    expansion_coefficient: DimensionalFunction_ThermalExpansionRate | None = Field(
        validation_alias="expansionCoefficient", serialization_alias="expansionCoefficient", default=None
    )
    reference_temperature: Dimensional_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
