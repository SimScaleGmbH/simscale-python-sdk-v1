from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__rotation_speed import Dimensional_RotationSpeed
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RotatingWall(SimScaleModel):
    name: str | None = Field(default=None)
    origin: DimensionalVector_Length | None = Field(default=None)
    axis: DimensionalVector_Length | None = Field(default=None)
    rotational_velocity: Dimensional_RotationSpeed | None = Field(
        validation_alias="rotationalVelocity", serialization_alias="rotationalVelocity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
