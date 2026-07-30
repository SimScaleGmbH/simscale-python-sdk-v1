from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ScaleBodiesParameters(SimScaleModel):
    factor: float = Field(description="Scaling factor. Must be greater than zero.")
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
