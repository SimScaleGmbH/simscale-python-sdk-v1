from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class SilverBirch(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SILVER_BIRCH",
        description="Schema name: SilverBirch",
    )
    average_tree_height: Dimensional_Length | None = Field(
        validation_alias="averageTreeHeight", serialization_alias="averageTreeHeight", default=None
    )
