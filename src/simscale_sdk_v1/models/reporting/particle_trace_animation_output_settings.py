from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.resolution_info import ResolutionInfo


class ParticleTraceAnimationOutputSettings(SimScaleModel):
    name: str
    format: Literal["GIF", "MP4"] = Field(default="GIF")
    resolution: ResolutionInfo
    frame_rate: int = Field(validation_alias="frameRate", serialization_alias="frameRate", default=20)
    show_legend: bool = Field(validation_alias="showLegend", serialization_alias="showLegend", default=True)
    show_cube: bool = Field(validation_alias="showCube", serialization_alias="showCube", default=True)
    background_color: Color | None = Field(
        validation_alias="backgroundColor", serialization_alias="backgroundColor", default=None
    )
    type_: str = Field(validation_alias="type", serialization_alias="type", default="PARTICLE_TRACE")
    frame_index: int | None = Field(
        validation_alias="frameIndex",
        serialization_alias="frameIndex",
        default=None,
        description="Default is the last frame (time step) in the result.",
    )
    steps: int = Field(default=300, description="The number of steps to generate for the particle trace animation.")
