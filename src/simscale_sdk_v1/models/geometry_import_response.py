from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.status import Status


class GeometryImportResponse(SimScaleModel):
    geometry_import_id: str = Field(
        validation_alias="geometryImportId",
        serialization_alias="geometryImportId",
        description="The ID of the geometry import operation.",
    )
    status: Status
    geometry_id: str | None = Field(
        validation_alias="geometryId",
        serialization_alias="geometryId",
        default=None,
        description="The ID of the imported geometry when the import succeeded.",
    )
    failure_reason: LogEntry | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
