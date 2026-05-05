from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class Sycamore(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="SYCAMORE", description="Schema name: Sycamore"
    )
    average_tree_height: Dimensional_Length | None = Field(
        validation_alias="averageTreeHeight", serialization_alias="averageTreeHeight", default=None
    )
