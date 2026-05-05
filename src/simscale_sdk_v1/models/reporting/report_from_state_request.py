from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.report_from_state_properties import ReportFromStateProperties


class ReportFromStateRequest(SimScaleModel):
    name: str = Field(description="The name of the report.")
    description: str | None = Field(default=None, description="The description of the report.")
    result_ids: list[str] = Field(
        validation_alias="resultIds",
        serialization_alias="resultIds",
        description="The IDs of the results for which the report should be created.",
    )
    report_from_state_properties: ReportFromStateProperties = Field(
        validation_alias="reportFromStateProperties", serialization_alias="reportFromStateProperties"
    )
    report_id: str | None = Field(
        validation_alias="reportId",
        serialization_alias="reportId",
        default=None,
        description="If provided, the newly created report will have this value for its UUID.",
    )
