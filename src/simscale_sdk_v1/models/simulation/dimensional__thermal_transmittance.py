from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_ThermalTransmittance(SimScaleModel):
    value: float | None = Field(default=None)
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
