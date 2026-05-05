from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Interference(SimScaleModel):
    target: str = Field(description="Internal name of the solid region.")
    tool: str = Field(description="Internal name of the solid region.")
