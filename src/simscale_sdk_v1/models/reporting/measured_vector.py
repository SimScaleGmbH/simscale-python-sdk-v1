from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MeasuredVector(SimScaleModel):
    """A 3-component spatial vector (e.g. a position or a centroid) paired with its length unit."""

    value: list[float] | None = Field(default=None)
    unit: str | None = Field(default=None)
