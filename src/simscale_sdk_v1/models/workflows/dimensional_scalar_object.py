from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalScalarObject(SimScaleModel):
    """A dimensional scalar is represented by a real number and a unit.                  By convention, all operators return a DimensionalScalar in base SI units.                  The interface for certain functions accepts Numbers instead of Doubles so that we can have operations with all types of numbers. If this proves to be a performance bottleneck, we can re-assess."""

    unit: str | None = Field(default=None)
    value: float | None = Field(default=None)
