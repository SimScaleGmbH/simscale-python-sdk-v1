from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CylindersVisualizationStyle(SimScaleModel):
    representation: str = Field(default="CYLINDERS", description="The representation to use for particle traces.")
