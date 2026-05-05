from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_expansion_rate_value import (
    OneOf_DimensionalFunction_ThermalExpansionRateValue,
)


class DimensionalFunction_ThermalExpansionRate(SimScaleModel):
    value: OneOf_DimensionalFunction_ThermalExpansionRateValue | None = Field(default=None)
    unit: Literal["1/K", "1/°F"]
