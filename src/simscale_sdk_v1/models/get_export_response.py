from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GetExportResponse(SimScaleModel):
    export_id: str | None = Field(validation_alias="exportId", serialization_alias="exportId", default=None)
    status: str | None = Field(
        default=None,
        description="RUNNING - Export is still in progress DONE - Export is done and ready for download FAILED - Export failed, please retry or contact support EXPIRED - Export is expired, please trigger a new export for the result",
    )
    url: str | None = Field(
        default=None, description="The temporary url for downloading the exported result, only set when status is DONE."
    )
    url_expires_at: str | None = Field(
        validation_alias="urlExpiresAt",
        serialization_alias="urlExpiresAt",
        default=None,
        description="Timestamp that the url will be expired, only set when status is DONE. Note that this timestamp is not a guarantee, if the url expired prematurely, please retry this request to get a new one.",
    )
    error_code: str | None = Field(validation_alias="errorCode", serialization_alias="errorCode", default=None)
