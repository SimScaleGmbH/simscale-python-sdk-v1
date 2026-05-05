from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WindData(SimScaleModel):
    name: str = Field(description="The name of the newly created simulation run.")
