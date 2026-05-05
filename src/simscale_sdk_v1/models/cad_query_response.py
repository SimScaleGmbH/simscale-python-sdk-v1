from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.cad_query_result import CadQueryResult
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.status import Status


class CadQueryResponse(SimScaleModel):
    status: Status | None = Field(default=None)
    result: CadQueryResult | None = Field(default=None)
    failure_reason: LogEntry | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
