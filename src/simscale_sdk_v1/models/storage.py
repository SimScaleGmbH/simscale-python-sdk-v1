from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Storage(SimScaleModel):
    url: str | None = Field(default=None, description="The URL of the temporary storage location.")
    storage_id: str | None = Field(
        validation_alias="storageId", serialization_alias="storageId", default=None, description="The storage ID."
    )
    expires_at: datetime | None = Field(
        validation_alias="expiresAt", serialization_alias="expiresAt", default=None, description="The expiration time."
    )
