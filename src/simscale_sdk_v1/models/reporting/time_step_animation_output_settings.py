from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.resolution_info import ResolutionInfo


class TimeStepAnimationOutputSettings(SimScaleModel):
    name: str
    format: Literal["GIF", "MP4"] = Field(default="GIF")
    resolution: ResolutionInfo
    frame_rate: int = Field(validation_alias="frameRate", serialization_alias="frameRate", default=20)
    show_legend: bool = Field(validation_alias="showLegend", serialization_alias="showLegend", default=True)
    show_cube: bool = Field(validation_alias="showCube", serialization_alias="showCube", default=True)
    background_color: Color | None = Field(
        validation_alias="backgroundColor", serialization_alias="backgroundColor", default=None
    )
    type_: str = Field(validation_alias="type", serialization_alias="type", default="TIME_STEP")
    from_frame_index: int = Field(validation_alias="fromFrameIndex", serialization_alias="fromFrameIndex", default=0)
    to_frame_index: int | None = Field(
        validation_alias="toFrameIndex",
        serialization_alias="toFrameIndex",
        default=None,
        description="Index of the last frame to include (inclusive). Defaults to the last available frame when not provided.",
    )
    skip_frames: int = Field(validation_alias="skipFrames", serialization_alias="skipFrames", default=0)
