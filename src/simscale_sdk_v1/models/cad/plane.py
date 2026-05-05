from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector import Vector


class Plane(SimScaleModel):
    """Plane with unit."""

    point: Vector
    normal: Vector
    unit: Literal["m", "cm", "mm", "yd", "ft", "in"] = Field(description="Unit of measurement.")
