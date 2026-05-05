from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.resolution_info import ResolutionInfo


class ShapeAnimationOutputSettings(SimScaleModel):
    name: str
    format: Literal["GIF", "MP4"] = Field(default="GIF")
    resolution: ResolutionInfo
    frame_rate: int = Field(validation_alias="frameRate", serialization_alias="frameRate", default=20)
    show_legend: bool = Field(validation_alias="showLegend", serialization_alias="showLegend", default=True)
    show_cube: bool = Field(validation_alias="showCube", serialization_alias="showCube", default=True)
    background_color: Color | None = Field(
        validation_alias="backgroundColor", serialization_alias="backgroundColor", default=None
    )
    type_: str | None = Field(validation_alias="type", serialization_alias="type", default="SHAPE")
    frame_index: int | None = Field(
        validation_alias="frameIndex",
        serialization_alias="frameIndex",
        default=None,
        description="Frame (or frequency) for which to create a mode shape animation.Default is the last frame in the result.",
    )
    steps: int = Field(default=30, description="The number of steps to generate for the shape animation")
    range: Literal["FULL", "HALF", "QUARTER"] = Field(
        default="FULL",
        description="How to deform the model for the animation. FULL implies animating from the original, undeformed shape to the maximum displaced position, then back to original shape; do the same for the negative maximum deformation, then back (x_0 -> +x_max -> x_0 -> -x_max -> x_0). HALF implies animating from the original, undeformed shape to the maximum displaced position, then back to original shape (x_0 -> +x_max -> x_0). QUARTER implies animating from the original, undeformed shape to the maxiumum displaced position (x_0 -> +x_max)",
    )
