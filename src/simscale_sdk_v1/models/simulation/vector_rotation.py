from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.dimensional_vector__rotation_speed import DimensionalVector_RotationSpeed


class VectorRotation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VECTOR_ROTATION",
        description="Schema name: VectorRotation",
    )
    rotation_center: DimensionalVector_Length | None = Field(
        validation_alias="rotationCenter", serialization_alias="rotationCenter", default=None
    )
    angular_velocity: DimensionalVector_RotationSpeed | None = Field(
        validation_alias="angularVelocity", serialization_alias="angularVelocity", default=None
    )
