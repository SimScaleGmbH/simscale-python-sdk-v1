from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.filters import Filters
from simscale_sdk_v1.models.reporting.model_settings import ModelSettings
from simscale_sdk_v1.models.reporting.one_of_camera_settings import OneOfCameraSettings
from simscale_sdk_v1.models.reporting.screenshot_output_settings import ScreenshotOutputSettings


class ScreenshotReportProperties(SimScaleModel):
    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="SCREENSHOT")
    model_settings: ModelSettings = Field(validation_alias="modelSettings", serialization_alias="modelSettings")
    filters: Filters | None = Field(default=None)
    camera_settings: OneOfCameraSettings = Field(
        validation_alias="cameraSettings", serialization_alias="cameraSettings"
    )
    output_settings: ScreenshotOutputSettings = Field(
        validation_alias="outputSettings", serialization_alias="outputSettings"
    )
