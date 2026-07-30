from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector import Vector


class Cylinder(SimScaleModel):
    """Cylinder with unit."""

    center: Vector
    axis: Vector
    radius: float = Field(description="Radius of the cylinder. Uses the sibling `unit` field.")
    height: float = Field(description="Height of the cylinder. Uses the sibling `unit` field.")
    unit: Literal["m", "cm", "mm", "yd", "ft", "in"] = Field(description="Unit of measurement.")
