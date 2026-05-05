from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_ThermalConductivity(SimScaleModel):
    value: float | None = Field(default=None)
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
