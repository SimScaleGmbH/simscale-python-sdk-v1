from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.filters import Filters
from simscale_sdk_v1.models.reporting.model_settings import ModelSettings
from simscale_sdk_v1.models.reporting.one_of_animation_output_settings import OneOfAnimationOutputSettings
from simscale_sdk_v1.models.reporting.one_of_camera_settings import OneOfCameraSettings


class AnimationReportProperties(SimScaleModel):
    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="ANIMATION")
    model_settings: ModelSettings = Field(validation_alias="modelSettings", serialization_alias="modelSettings")
    filters: Filters | None = Field(default=None)
    camera_settings: OneOfCameraSettings = Field(
        validation_alias="cameraSettings", serialization_alias="cameraSettings"
    )
    output_settings: OneOfAnimationOutputSettings = Field(
        validation_alias="outputSettings", serialization_alias="outputSettings"
    )
