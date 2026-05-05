from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class Point(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="POINT", description="Schema name: Point"
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    center: DimensionalVector_Length | None = Field(default=None)
