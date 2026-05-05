from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class LocalHalfSpace(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LOCAL_HALF_SPACE",
        description="Schema name: LocalHalfSpace",
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    orientation_reference: Literal["GEOMETRY", "FLOW_DOMAIN"] | None = Field(
        validation_alias="orientationReference", serialization_alias="orientationReference", default="GEOMETRY"
    )
    reference_point: DimensionalVector_Length | None = Field(
        validation_alias="referencePoint", serialization_alias="referencePoint", default=None
    )
    normal: DimensionalVector_Length | None = Field(default=None)
