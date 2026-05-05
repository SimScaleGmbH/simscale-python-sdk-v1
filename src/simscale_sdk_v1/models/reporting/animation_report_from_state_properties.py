from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.one_of_animation_output_settings import OneOfAnimationOutputSettings
from simscale_sdk_v1.models.reporting.state_metadata import StateMetadata


class AnimationReportFromStateProperties(SimScaleModel):
    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="ANIMATION")
    state_metadata: StateMetadata = Field(validation_alias="stateMetadata", serialization_alias="stateMetadata")
    output_settings: OneOfAnimationOutputSettings = Field(
        validation_alias="outputSettings", serialization_alias="outputSettings"
    )
