from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__turbulence_kinetic_energy import (
    DimensionalFunction_TurbulenceKineticEnergy,
)


class TurbulenceKineticEnergyTIBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TURBULENCE_KINETIC_ENERGY",
        description="Schema name: TurbulenceKineticEnergyTIBC",
    )
    value: DimensionalFunction_TurbulenceKineticEnergy | None = Field(default=None)
