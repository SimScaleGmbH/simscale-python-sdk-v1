from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class Square(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="SQUARE", description="Schema name: Square"
    )
    strand_width: Dimensional_Length | None = Field(
        validation_alias="strandWidth", serialization_alias="strandWidth", default=None
    )
