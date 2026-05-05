from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class LocalCartesianBox(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LOCAL_CARTESIAN_BOX",
        description="Schema name: LocalCartesianBox",
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    orientation_reference: Literal["GEOMETRY", "FLOW_DOMAIN"] | None = Field(
        validation_alias="orientationReference", serialization_alias="orientationReference", default="GEOMETRY"
    )
    min: DimensionalVector_Length | None = Field(default=None)
    max: DimensionalVector_Length | None = Field(default=None)
