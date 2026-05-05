from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__thermal_transmittance_value import (
    OneOf_DimensionalFunction_ThermalTransmittanceValue,
)


class DimensionalFunction_ThermalTransmittance(SimScaleModel):
    value: OneOf_DimensionalFunction_ThermalTransmittanceValue | None = Field(default=None)
    unit: Literal[
        "W/(K·m²)",
        "Btu/(s·in²·°F)",
        "W/(K·mm²)",
        "W/(K·cm²)",
        "Btu/(h·in²·°F)",
        "Btu/(min·in²·°F)",
        "Btu/(s·ft²·°F)",
        "Btu/(min·ft²·°F)",
    ]
