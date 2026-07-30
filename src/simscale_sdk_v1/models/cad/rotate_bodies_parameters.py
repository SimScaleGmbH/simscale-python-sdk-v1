from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.axis import Axis


class RotateBodiesParameters(SimScaleModel):
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
    axis: Axis
    angle: float = Field(description="Angle or rotation in degrees.")
    copy_bodies: bool = Field(
        description="If true, the operation creates new bodies instead of modifying the selected ones; if false, the selected bodies are modified in place."
    )
