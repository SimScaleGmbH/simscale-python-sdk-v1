from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__rotation_speed import DimensionalFunction_RotationSpeed
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MRFRotatingZone(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MULTI_REFERENCE_FRAME",
        description="Schema name: MRFRotatingZone",
    )
    name: str | None = Field(default=None)
    origin: DimensionalVector_Length | None = Field(default=None)
    axis: DimensionalVector_Length | None = Field(default=None)
    angular_velocity: DimensionalFunction_RotationSpeed | None = Field(
        validation_alias="angularVelocity", serialization_alias="angularVelocity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
