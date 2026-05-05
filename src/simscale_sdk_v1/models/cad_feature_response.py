from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.status import Status


class CadFeatureResponse(SimScaleModel):
    cad_state_id: str | None = Field(
        validation_alias="cadStateId",
        serialization_alias="cadStateId",
        default=None,
        description="The ID of the CAD state once completed.",
    )
    cad_feature_id: str | None = Field(
        validation_alias="cadFeatureId",
        serialization_alias="cadFeatureId",
        default=None,
        description="The ID of the CAD feature once completed.",
    )
    status: Status
    failure_reason: LogEntry | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
