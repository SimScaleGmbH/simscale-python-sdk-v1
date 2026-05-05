from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class CartesianBox(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CARTESIAN_BOX",
        description="Schema name: CartesianBox",
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    min: DimensionalVector_Length | None = Field(default=None)
    max: DimensionalVector_Length | None = Field(default=None)
