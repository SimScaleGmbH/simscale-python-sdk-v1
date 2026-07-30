from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.animation_report_properties import AnimationReportProperties
from simscale_sdk_v1.models.reporting.screenshot_report_properties import ScreenshotReportProperties
from simscale_sdk_v1.models.reporting.statistics_global_min_max_report_properties import (
    StatisticsGlobalMinMaxReportProperties,
)
from simscale_sdk_v1.models.reporting.statistics_report_properties import StatisticsReportProperties

_REPORT_PROPERTIES_VARIANTS: dict[str, type] = {
    "ANIMATION": AnimationReportProperties,
    "SCREENSHOT": ScreenshotReportProperties,
    "STATISTICS": StatisticsReportProperties,
    "STATISTICS_GLOBAL_MIN_MAX": StatisticsGlobalMinMaxReportProperties,
}

ReportProperties = Annotated[
    Union[
        AnimationReportProperties,
        ScreenshotReportProperties,
        StatisticsReportProperties,
        StatisticsGlobalMinMaxReportProperties,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="reportType",
            variants=_REPORT_PROPERTIES_VARIANTS,
        )
    ),
]
