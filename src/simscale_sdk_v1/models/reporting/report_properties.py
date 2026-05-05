from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.animation_report_properties import AnimationReportProperties
from simscale_sdk_v1.models.reporting.screenshot_report_properties import ScreenshotReportProperties
from simscale_sdk_v1.models.reporting.statistics_report_properties import StatisticsReportProperties

_REPORT_PROPERTIES_VARIANTS: dict[str, type] = {
    "ANIMATION": AnimationReportProperties,
    "SCREENSHOT": ScreenshotReportProperties,
    "STATISTICS": StatisticsReportProperties,
}

ReportProperties = Annotated[
    Union[AnimationReportProperties, ScreenshotReportProperties, StatisticsReportProperties],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="reportType",
            variants=_REPORT_PROPERTIES_VARIANTS,
        )
    ),
]
