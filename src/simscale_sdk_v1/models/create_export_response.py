from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateExportResponse(SimScaleModel):
    export_id: str | None = Field(validation_alias="exportId", serialization_alias="exportId", default=None)
    result_id: str | None = Field(
        validation_alias="resultId",
        serialization_alias="resultId",
        default=None,
        description="The result to be exported",
    )
    format: str | None = Field(default=None, description="The format to export to")
    status: str | None = Field(
        default=None,
        description="RUNNING - Export is still in progress DONE - Export is done and ready for download FAILED - Export failed, please retry or contact support EXPIRED - Export is expired, please trigger a new export for the result",
    )
    error_code: str | None = Field(validation_alias="errorCode", serialization_alias="errorCode", default=None)
