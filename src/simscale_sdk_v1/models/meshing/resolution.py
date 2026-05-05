from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Resolution(SimScaleModel):
    x: int = Field(description="Specify the number of cells in x direction for the base mesh.")
    y: int = Field(description="Specify the number of cells in y direction for the base mesh.")
    z: int = Field(description="Specify the number of cells in z direction for the base mesh.")
