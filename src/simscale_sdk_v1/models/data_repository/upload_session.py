from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class UploadSession(SimScaleModel):
    """Initialized upload session."""

    storage_id: str | None = Field(validation_alias="storageId", serialization_alias="storageId", default=None)
