from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_expansion_rate import (
    DimensionalFunction_ThermalExpansionRate,
)


class IsotropicExpansion(SimScaleModel):
    """Define the directional dependency of this property. Isotropic means directionally independent."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Define the directional dependency of this property. Isotropic means directionally independent.  Schema name: IsotropicExpansion",
    )
    expansion_coefficient: DimensionalFunction_ThermalExpansionRate | None = Field(
        validation_alias="expansionCoefficient", serialization_alias="expansionCoefficient", default=None
    )
    reference_temperature: Dimensional_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
