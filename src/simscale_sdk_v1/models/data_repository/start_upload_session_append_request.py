from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StartUploadSessionAppendRequest(SimScaleModel):
    """Request to start appending one chunk to an initialized upload session."""

    size: int | None = Field(default=None)
