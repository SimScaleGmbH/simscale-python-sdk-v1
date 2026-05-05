from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RenameCadRequest(SimScaleModel):
    name: str = Field(description="New CAD name.")
