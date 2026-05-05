from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DownloadOriginalCadResponse(SimScaleModel):
    url: str | None = Field(
        default=None, description="The temporary url for downloading the the originally imported CAD file."
    )
    url_expires_at: str | None = Field(
        validation_alias="urlExpiresAt",
        serialization_alias="urlExpiresAt",
        default=None,
        description="Expiration timestamp of the URL. Note that this timestamp is not a guarantee, if the url expired prematurely, please retry this request to get a new one.",
    )
