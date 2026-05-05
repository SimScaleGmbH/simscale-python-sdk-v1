from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StateShapeAnimationOutputSettings(SimScaleModel):
    type_: str = Field(validation_alias="type", serialization_alias="type", default="SHAPE")
    show_legend: bool = Field(
        validation_alias="showLegend",
        serialization_alias="showLegend",
        description="True if any scalarSettings entry in the state has legendVisibilityMode set to AUTO (1) or ALWAYS (2). False if all entries are set to NEVER (0) or no scalarSettings are present.",
    )
    frame_index: int = Field(
        validation_alias="frameIndex",
        serialization_alias="frameIndex",
        description="Frame (or frequency) for which to create a mode shape animation.",
    )
    steps: int = Field(description="The number of steps to generate for the shape animation.")
    range: Literal["FULL", "HALF", "QUARTER"] = Field(
        description="How to deform the model for the animation. FULL (x0 -> +xmax -> x0 -> -xmax -> x0), HALF (x0 -> +xmax -> x0), QUARTER (x0 -> +xmax)."
    )
