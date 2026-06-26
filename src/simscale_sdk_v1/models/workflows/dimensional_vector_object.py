from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.vector import Vector


class DimensionalVectorObject(SimScaleModel):
    """A dimensional vector is represented by a 3D vector and a unit.                  By convention, all operators return a DimensionalVector in base SI units.                  The interface for certain functions accepts Numbers instead of Doubles so that we can have operations with all types of numbers. If this proves to be a performance bottleneck, we can re-assess."""

    unit: str | None = Field(default=None)
    vector: Vector | None = Field(default=None)
