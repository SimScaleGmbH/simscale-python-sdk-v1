from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.data_repository.http_header import HttpHeader


class PresignedRequest(SimScaleModel):
    """Pre-signed HTTP request."""

    headers: list[HttpHeader] | None = Field(default=None)
    url: str | None = Field(default=None)
