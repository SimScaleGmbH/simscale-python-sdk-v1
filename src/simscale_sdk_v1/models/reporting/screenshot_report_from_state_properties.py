from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.screenshot_output_settings import ScreenshotOutputSettings
from simscale_sdk_v1.models.reporting.state_metadata import StateMetadata


class ScreenshotReportFromStateProperties(SimScaleModel):
    report_type: str = Field(validation_alias="reportType", serialization_alias="reportType", default="SCREENSHOT")
    state_metadata: StateMetadata = Field(validation_alias="stateMetadata", serialization_alias="stateMetadata")
    output_settings: ScreenshotOutputSettings = Field(
        validation_alias="outputSettings", serialization_alias="outputSettings"
    )
