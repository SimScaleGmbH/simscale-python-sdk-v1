from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__heat_flux_value import (
    OneOf_DimensionalFunction_HeatFluxValue,
)


class DimensionalFunction_HeatFlux(SimScaleModel):
    value: OneOf_DimensionalFunction_HeatFluxValue | None = Field(default=None)
    unit: Literal[
        "W/m²",
        "Btu/(s·in²)",
        "W/mm²",
        "W/cm²",
        "Btu/(h·ft²)",
        "Btu/(min·ft²)",
        "Btu/(s·ft²)",
        "Btu/(h·in²)",
        "Btu/(min·in²)",
    ]
