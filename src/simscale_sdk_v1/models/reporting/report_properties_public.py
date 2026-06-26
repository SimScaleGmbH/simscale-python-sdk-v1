from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.animation_report_properties import AnimationReportProperties
from simscale_sdk_v1.models.reporting.screenshot_report_properties import ScreenshotReportProperties
from simscale_sdk_v1.models.reporting.statistics_report_properties_public import StatisticsReportPropertiesPublic

# Public counterpart of ReportProperties whose STATISTICS variant omits the server-resolved resolution hints (cadAssociations, topologyLabelByName). Used by the public ReportResponse; the report request and the internal report representation use ReportProperties, which carries those fields.
_REPORT_PROPERTIES_PUBLIC_VARIANTS: dict[str, type] = {
    "ANIMATION": AnimationReportProperties,
    "SCREENSHOT": ScreenshotReportProperties,
    "STATISTICS": StatisticsReportPropertiesPublic,
}

ReportPropertiesPublic = Annotated[
    Union[AnimationReportProperties, ScreenshotReportProperties, StatisticsReportPropertiesPublic],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="reportType",
            variants=_REPORT_PROPERTIES_PUBLIC_VARIANTS,
        )
    ),
]
