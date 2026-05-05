from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class HalfSpace(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="HALF_SPACE", description="Schema name: HalfSpace"
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    reference_point: DimensionalVector_Length | None = Field(
        validation_alias="referencePoint", serialization_alias="referencePoint", default=None
    )
    normal: DimensionalVector_Length | None = Field(default=None)
