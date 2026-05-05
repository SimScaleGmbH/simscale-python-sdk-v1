from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__total_thermal_transmittance_value import (
    OneOf_DimensionalFunction_TotalThermalTransmittanceValue,
)


class DimensionalFunction_TotalThermalTransmittance(SimScaleModel):
    value: OneOf_DimensionalFunction_TotalThermalTransmittanceValue | None = Field(default=None)
    unit: Literal["W/K", "Btu/(s·°F)"]
