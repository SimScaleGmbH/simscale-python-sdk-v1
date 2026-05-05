from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__speed import DimensionalFunction_Speed


class FixedMagnitudeVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE_NO_EXPRESSION",
        description="Schema name: FixedMagnitudeVBC",
    )
    value: DimensionalFunction_Speed | None = Field(default=None)
