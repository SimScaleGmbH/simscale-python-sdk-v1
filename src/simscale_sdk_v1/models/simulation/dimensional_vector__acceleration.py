from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.decimal_vector import DecimalVector


class DimensionalVector_Acceleration(SimScaleModel):
    value: DecimalVector | None = Field(default=None)
    unit: Literal["m/s²", "in/s²", "G"]
