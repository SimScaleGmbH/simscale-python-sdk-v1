from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.plane import Plane


class SplitBodiesParameters(SimScaleModel):
    plane: Plane
    keep_both: bool = Field(
        description="Controls the split. If `true`, both sides of the bodies are kept; otherwise, only the side facing the normal is retained."
    )
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
