from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.report_from_state_properties import ReportFromStateProperties
from simscale_sdk_v1.models.reporting.report_properties import ReportProperties


class InternalReportResponse(SimScaleModel):
    """Report properties as returned by the internal report endpoint that postproc-result-query reads. Its reportProperties uses the full ReportProperties, including the server-resolved resolution hints (cadAssociations, topologyLabelByName) that the public ReportResponse omits. Only the fields the batch job needs are exposed here; the public-facing report fields (status, download, statisticsResult, ...) live on ReportResponse."""

    report_properties: ReportProperties | None = Field(
        validation_alias="reportProperties", serialization_alias="reportProperties", default=None
    )
    report_from_state_properties: ReportFromStateProperties | None = Field(
        validation_alias="reportFromStateProperties", serialization_alias="reportFromStateProperties", default=None
    )
