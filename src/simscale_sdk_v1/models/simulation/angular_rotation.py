from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__rotation_speed import DimensionalFunction_RotationSpeed
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class AngularRotation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ANGULAR_ROTATION",
        description="Schema name: AngularRotation",
    )
    rotation_center: DimensionalVector_Length | None = Field(
        validation_alias="rotationCenter", serialization_alias="rotationCenter", default=None
    )
    rotation_axis: DimensionalVector_Length | None = Field(
        validation_alias="rotationAxis", serialization_alias="rotationAxis", default=None
    )
    angular_velocity: DimensionalFunction_RotationSpeed | None = Field(
        validation_alias="angularVelocity", serialization_alias="angularVelocity", default=None
    )
