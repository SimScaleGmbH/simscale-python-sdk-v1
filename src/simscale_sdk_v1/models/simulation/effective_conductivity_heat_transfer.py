from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_conductivity import (
    DimensionalFunction_ThermalConductivity,
)


class EffectiveConductivityHeatTransfer(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="EFFECTIVE_CONDUCTIVITY_HEAT_TRANSFER",
        description="Schema name: EffectiveConductivityHeatTransfer",
    )
    effective_thermal_conductivity: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="effectiveThermalConductivity",
        serialization_alias="effectiveThermalConductivity",
        default=None,
    )
