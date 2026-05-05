from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class CustomOrientation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomOrientation",
    )
    unit_vector1: DimensionalVector_Length | None = Field(
        validation_alias="unitVector1", serialization_alias="unitVector1", default=None
    )
    unit_vector2: DimensionalVector_Length | None = Field(
        validation_alias="unitVector2", serialization_alias="unitVector2", default=None
    )
