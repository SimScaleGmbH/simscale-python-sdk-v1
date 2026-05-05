from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.animation_report_from_state_properties import AnimationReportFromStateProperties
from simscale_sdk_v1.models.reporting.screenshot_report_from_state_properties import ScreenshotReportFromStateProperties

_REPORT_FROM_STATE_PROPERTIES_VARIANTS: dict[str, type] = {
    "ANIMATION": AnimationReportFromStateProperties,
    "SCREENSHOT": ScreenshotReportFromStateProperties,
}

ReportFromStateProperties = Annotated[
    Union[AnimationReportFromStateProperties, ScreenshotReportFromStateProperties],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="reportType",
            variants=_REPORT_FROM_STATE_PROPERTIES_VARIANTS,
        )
    ),
]
