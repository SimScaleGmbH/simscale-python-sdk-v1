from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class HttpHeader(SimScaleModel):
    """HTTP header."""

    name: str | None = Field(default=None)
    value: str | None = Field(default=None)
