from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.box import Box


class BoxWithUnit(SimScaleModel):
    """Axis-aligned box with unit."""

    box: Box
    unit: Literal["m", "cm", "mm", "yd", "ft", "in"] = Field(description="Unit of measurement.")
