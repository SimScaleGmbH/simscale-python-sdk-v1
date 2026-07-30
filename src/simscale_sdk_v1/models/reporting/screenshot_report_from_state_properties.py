from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.one_of_camera_settings import OneOfCameraSettings
from simscale_sdk_v1.models.reporting.screenshot_output_settings import ScreenshotOutputSettings
from simscale_sdk_v1.models.reporting.state_metadata import StateMetadata
from simscale_sdk_v1.models.reporting.state_overrides import StateOverrides


class ScreenshotReportFromStateProperties(SimScaleModel):
    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="SCREENSHOT")
    state_metadata: StateMetadata = Field(validation_alias="stateMetadata", serialization_alias="stateMetadata")
    output_settings: ScreenshotOutputSettings = Field(
        validation_alias="outputSettings", serialization_alias="outputSettings"
    )
    camera_override: OneOfCameraSettings | None = Field(
        validation_alias="cameraOverride", serialization_alias="cameraOverride", default=None
    )
    state_overrides: StateOverrides | None = Field(
        validation_alias="stateOverrides", serialization_alias="stateOverrides", default=None
    )
    persist: bool | None = Field(
        default=True,
        description="When false, the rendered screenshot is not registered back into the project (ephemeral). Defaults to true.",
    )
