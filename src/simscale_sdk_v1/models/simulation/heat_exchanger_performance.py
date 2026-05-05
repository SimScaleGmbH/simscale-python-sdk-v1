from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__total_thermal_transmittance import (
    DimensionalFunction_TotalThermalTransmittance,
)


class HeatExchangerPerformance(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HEAT_EXCHANGER_PERFORMANCE",
        description="Schema name: HeatExchangerPerformance",
    )
    ref_temperature: DimensionalFunction_Temperature | None = Field(
        validation_alias="refTemperature", serialization_alias="refTemperature", default=None
    )
    performance: DimensionalFunction_TotalThermalTransmittance | None = Field(default=None)
