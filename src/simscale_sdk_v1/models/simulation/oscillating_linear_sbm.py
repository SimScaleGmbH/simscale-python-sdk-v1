from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__rotation_speed import Dimensional_RotationSpeed
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class OscillatingLinearSBM(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OSCILLATING_LINEAR_MOTION",
        description="Schema name: OscillatingLinearSBM",
    )
    name: str | None = Field(default=None)
    amplitude: DimensionalVector_Length | None = Field(default=None)
    angular_velocity: Dimensional_RotationSpeed | None = Field(
        validation_alias="angularVelocity", serialization_alias="angularVelocity", default=None
    )
