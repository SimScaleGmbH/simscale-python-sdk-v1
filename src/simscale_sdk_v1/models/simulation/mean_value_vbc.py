from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed


class MeanValueVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_MEAN",
        description="Schema name: MeanValueVBC",
    )
    value: DimensionalVector_Speed | None = Field(default=None)
