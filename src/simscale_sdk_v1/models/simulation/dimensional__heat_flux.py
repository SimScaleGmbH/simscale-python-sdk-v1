from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_HeatFlux(SimScaleModel):
    value: float | None = Field(default=None)
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
