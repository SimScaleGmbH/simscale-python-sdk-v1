from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FacetSplitBodiesParameters(SimScaleModel):
    angle: float = Field(description="Maximum split angle, in degrees.")
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
