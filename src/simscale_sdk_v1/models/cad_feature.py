from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.status import Status


class CadFeature(SimScaleModel):
    id: str | None = Field(default=None, description="The ID of the CAD feature.")
    type_: str | None = Field(
        validation_alias="type", serialization_alias="type", default=None, description="The type of the CAD feature."
    )
    parameters: dict[str, Any] | None = Field(default=None, description="The parameters of the CAD feature.")
    status: Status | None = Field(default=None)
    depth: int | None = Field(default=None, description="The depth of the CAD feature in the feature list.")
    failure_reason: LogEntry | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
