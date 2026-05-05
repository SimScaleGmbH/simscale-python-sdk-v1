from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class AbsoluteDistance(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE",
        description="Schema name: AbsoluteDistance",
    )
    absolute_distance: Dimensional_Length | None = Field(
        validation_alias="absoluteDistance", serialization_alias="absoluteDistance", default=None
    )
