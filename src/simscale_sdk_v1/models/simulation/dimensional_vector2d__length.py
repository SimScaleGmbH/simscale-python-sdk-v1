from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.decimal_vector2d import DecimalVector2d


class DimensionalVector2d_Length(SimScaleModel):
    value: DecimalVector2d | None = Field(default=None)
    unit: Literal["m", "in", "mm", "cm", "ft", "yd"]
