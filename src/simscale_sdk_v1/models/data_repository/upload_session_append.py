from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.data_repository.presigned_request import PresignedRequest


class UploadSessionAppend(SimScaleModel):
    """Append operation initialized for an upload session."""

    append_id: str | None = Field(validation_alias="appendId", serialization_alias="appendId", default=None)
    pre_signed_put_request: PresignedRequest | None = Field(
        validation_alias="preSignedPutRequest", serialization_alias="preSignedPutRequest", default=None
    )
