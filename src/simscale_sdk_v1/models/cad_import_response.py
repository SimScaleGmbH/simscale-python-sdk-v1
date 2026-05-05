from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.status import Status


class CadImportResponse(SimScaleModel):
    cad_id: str = Field(validation_alias="cadId", serialization_alias="cadId", description="The ID of the CAD.")
    status: Status
    cad_state_id: str = Field(
        validation_alias="cadStateId",
        serialization_alias="cadStateId",
        description="The ID of the current CAD state. It can point to an empty CAD state in case the import is running or failed.",
    )
    failure_reason: LogEntry | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
