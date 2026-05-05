from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_conductivity_value import (
    OneOf_DimensionalFunction_ThermalConductivityValue,
)


class DimensionalFunction_ThermalConductivity(SimScaleModel):
    value: OneOf_DimensionalFunction_ThermalConductivityValue | None = Field(default=None)
    unit: Literal[
        "W/(m·K)",
        "Btu/(s·in·°F)",
        "W/(mm·K)",
        "W/(cm·K)",
        "Btu/(min·in·°F)",
        "Btu/(h·in·°F)",
        "Btu/(s·ft·°F)",
        "Btu/(min·ft·°F)",
        "Btu/(h·ft·°F)",
    ]
