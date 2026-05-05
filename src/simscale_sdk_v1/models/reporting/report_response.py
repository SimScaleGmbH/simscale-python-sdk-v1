from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.download_info import DownloadInfo
from simscale_sdk_v1.models.reporting.report_from_state_properties import ReportFromStateProperties
from simscale_sdk_v1.models.reporting.report_properties import ReportProperties
from simscale_sdk_v1.models.reporting.statistics_result_entry import StatisticsResultEntry


class ReportResponse(SimScaleModel):
    report_id: str = Field(
        validation_alias="reportId", serialization_alias="reportId", description="The ID of the report."
    )
    name: str = Field(description="The name of the report.")
    description: str | None = Field(default=None, description="The description of the report.")
    created_at: datetime = Field(
        validation_alias="createdAt", serialization_alias="createdAt", description="The time the report was created."
    )
    started_at: datetime | None = Field(
        validation_alias="startedAt",
        serialization_alias="startedAt",
        default=None,
        description="The time the report was started.",
    )
    finished_at: datetime | None = Field(
        validation_alias="finishedAt",
        serialization_alias="finishedAt",
        default=None,
        description="The time the report was finished.",
    )
    status: Literal["READY", "QUEUED", "RUNNING", "FINISHED", "CANCELED", "FAILED"] = Field(
        description="Status of the report operation."
    )
    result_ids: list[str] | None = Field(
        validation_alias="resultIds",
        serialization_alias="resultIds",
        default=None,
        description="The resultIds the report has been created for.",
    )
    report_properties: ReportProperties | None = Field(
        validation_alias="reportProperties", serialization_alias="reportProperties", default=None
    )
    report_from_state_properties: ReportFromStateProperties | None = Field(
        validation_alias="reportFromStateProperties", serialization_alias="reportFromStateProperties", default=None
    )
    download: DownloadInfo | None = Field(default=None)
    statistics_result: dict[str, StatisticsResultEntry] | None = Field(
        validation_alias="statisticsResult",
        serialization_alias="statisticsResult",
        default=None,
        description="Result of a STATISTICS report. Contains one entry per requested part identifier, part group identifier, or cutting plane identifier, each mapping to a StatisticsResultEntry. Null entries indicate that the part or plane was not found in the model.",
    )
    failure_reason: Any | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
