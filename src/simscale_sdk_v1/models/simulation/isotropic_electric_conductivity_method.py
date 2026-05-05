from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__electric_conductivity import (
    DimensionalFunction_ElectricConductivity,
)


class IsotropicElectricConductivityMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC_ELECTRIC_CONDUCTIVITY",
        description="Schema name: IsotropicElectricConductivityMethod",
    )
    electric_conductivity: DimensionalFunction_ElectricConductivity | None = Field(
        validation_alias="electricConductivity", serialization_alias="electricConductivity", default=None
    )
