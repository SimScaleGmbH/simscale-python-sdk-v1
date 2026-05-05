from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class BodyPath(SimScaleModel):
    assembly: str | None = Field(default=None)
    instance: str | None = Field(default=None)
