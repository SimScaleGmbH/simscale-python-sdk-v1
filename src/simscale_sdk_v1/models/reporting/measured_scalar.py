from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MeasuredScalar(SimScaleModel):
    """A scalar quantity paired with its unit string."""

    value: float | None = Field(default=None, description="The numeric value, or null when it could not be computed.")
    unit: str | None = Field(default=None)
