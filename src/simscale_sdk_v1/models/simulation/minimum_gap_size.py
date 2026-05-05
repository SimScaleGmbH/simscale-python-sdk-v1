from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class MinimumGapSize(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MINIMUM_GAP_SIZE",
        description="Schema name: MinimumGapSize",
    )
    minimum_gap_size: Dimensional_Length | None = Field(
        validation_alias="minimumGapSize", serialization_alias="minimumGapSize", default=None
    )
