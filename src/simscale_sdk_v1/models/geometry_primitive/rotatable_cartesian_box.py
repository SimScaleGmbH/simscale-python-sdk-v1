from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__angle import DimensionalVector_Angle
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class RotatableCartesianBox(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ROTATABLE_CARTESIAN_BOX",
        description="Schema name: RotatableCartesianBox",
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    min: DimensionalVector_Length | None = Field(default=None)
    max: DimensionalVector_Length | None = Field(default=None)
    rotation_point: DimensionalVector_Length | None = Field(
        validation_alias="rotationPoint", serialization_alias="rotationPoint", default=None
    )
    rotation_angles: DimensionalVector_Angle | None = Field(
        validation_alias="rotationAngles", serialization_alias="rotationAngles", default=None
    )
