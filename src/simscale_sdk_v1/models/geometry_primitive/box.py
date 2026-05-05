from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.geometry_primitive.decimal_vector import DecimalVector
from simscale_sdk_v1.models.geometry_primitive.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.geometry_primitive.dimensional_vector__length import DimensionalVector_Length


class Box(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="BOX", description="Schema name: Box"
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    scale: DecimalVector | None = Field(default=None)
    translation: DimensionalVector_Length | None = Field(default=None)
    rotation_axis: DimensionalVector_Length | None = Field(
        validation_alias="rotationAxis", serialization_alias="rotationAxis", default=None
    )
    rotation_angle: Dimensional_Angle | None = Field(
        validation_alias="rotationAngle", serialization_alias="rotationAngle", default=None
    )
