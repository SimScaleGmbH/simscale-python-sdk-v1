from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AdditionalDirectionalCells(SimScaleModel):
    x: int = Field(
        description="Specify the number of additional cells to be added in the X-direction. Note: additional cells in the negative X direction is not supported."
    )
    y: int = Field(
        description="Specify the number of additional cells to be added in the Y-direction. Note: additional cells in the negative Y direction is not supported."
    )
    z: int = Field(
        description="Specify the number of additional cells to be added in the Z-direction. Note: additional cells in the negative Z direction is not supported."
    )
