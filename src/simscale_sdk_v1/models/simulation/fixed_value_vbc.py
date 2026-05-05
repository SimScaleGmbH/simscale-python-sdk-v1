from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__speed import DimensionalVectorFunction_Speed


class FixedValueVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE",
        description="Schema name: FixedValueVBC",
    )
    value: DimensionalVectorFunction_Speed | None = Field(default=None)
