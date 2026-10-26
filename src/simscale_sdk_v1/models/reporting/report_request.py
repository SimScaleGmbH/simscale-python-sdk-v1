from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.report_properties import ReportProperties
from simscale_sdk_v1.models.reporting.report_trigger import ReportTrigger


class ReportRequest(SimScaleModel):
    """A report on a simulation result, given as exactly one entry in resultIds, or on a standalone RAMPS result such as a dataflow output, given as its dataId. Exactly one of the two must be given; the service rejects requests with both or neither."""

    name: str = Field(description="The name of the report.")
    description: str | None = Field(default=None, description="The description of the report.")
    result_ids: list[str] | None = Field(
        validation_alias="resultIds",
        serialization_alias="resultIds",
        default=None,
        description="The ID of the simulation result for which the report is created. Exactly one entry, or empty when dataId is given.",
    )
    data_id: str | None = Field(
        validation_alias="dataId",
        serialization_alias="dataId",
        default=None,
        description="The Data ID of the dataflow output for which the report is created. The data must belong to the project and reference a RAMPS result; the report then stores and returns that result's ID as rampsId. When set, resultIds must be empty. Supported for animation and screenshot reports; statistics reports are not supported yet.",
    )
    report_properties: ReportProperties = Field(
        validation_alias="reportProperties", serialization_alias="reportProperties"
    )
    report_id: str | None = Field(
        validation_alias="reportId",
        serialization_alias="reportId",
        default=None,
        description="If provided, the newly created report will have this value for its UUID.",
    )
    trigger: ReportTrigger | None = Field(default=None)
