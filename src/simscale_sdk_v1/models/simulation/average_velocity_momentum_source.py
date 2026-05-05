from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class AverageVelocityMomentumSource(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AVERAGE_VELOCITY",
        description="Schema name: AverageVelocityMomentumSource",
    )
    name: str | None = Field(default=None)
    average_velocity: DimensionalVector_Speed | None = Field(
        validation_alias="averageVelocity", serialization_alias="averageVelocity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
