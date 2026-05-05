from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StateTimeStepAnimationOutputSettings(SimScaleModel):
    type_: str = Field(validation_alias="type", serialization_alias="type", default="TIME_STEP")
    show_legend: bool = Field(
        validation_alias="showLegend",
        serialization_alias="showLegend",
        description="True if any scalarSettings entry in the state has legendVisibilityMode set to AUTO (1) or ALWAYS (2). False if all entries are set to NEVER (0) or no scalarSettings are present.",
    )
    from_frame_index: int = Field(validation_alias="fromFrameIndex", serialization_alias="fromFrameIndex")
    to_frame_index: int = Field(
        validation_alias="toFrameIndex",
        serialization_alias="toFrameIndex",
        description="Index of the last frame to include (inclusive).",
    )
    skip_frames: int = Field(validation_alias="skipFrames", serialization_alias="skipFrames")
