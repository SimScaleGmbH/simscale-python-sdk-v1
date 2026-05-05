from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class Sphere(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="SPHERE", description="Schema name: Sphere"
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    center: DimensionalVector_Length | None = Field(default=None)
    radius: Dimensional_Length | None = Field(default=None)
