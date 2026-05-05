from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.postprocessing.one_of_state_animation_output_settings import (
    OneOfStateAnimationOutputSettings,
)
from simscale_sdk_v1.models.postprocessing.state_screenshot_output_settings import StateScreenshotOutputSettings


class StateResponse(SimScaleModel):
    state_uuid: str = Field(
        validation_alias="stateUuid",
        serialization_alias="stateUuid",
        description="The unique identifier for the state (default, manually or automatically saved).",
    )
    state_name: str | None = Field(
        validation_alias="stateName",
        serialization_alias="stateName",
        default=None,
        description="State name, as provided in the workbench.",
    )
    state_description: str | None = Field(
        validation_alias="stateDescription",
        serialization_alias="stateDescription",
        default=None,
        description="Description of the state, as provided in the workbench.",
    )
    screenshot_output_settings: StateScreenshotOutputSettings | None = Field(
        validation_alias="screenshotOutputSettings", serialization_alias="screenshotOutputSettings", default=None
    )
    animation_output_settings: OneOfStateAnimationOutputSettings | None = Field(
        validation_alias="animationOutputSettings", serialization_alias="animationOutputSettings", default=None
    )
