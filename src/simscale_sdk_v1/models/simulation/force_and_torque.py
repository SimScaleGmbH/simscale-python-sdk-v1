from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ForceAndTorque(SimScaleModel):
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    torque_reference_point: DimensionalVector_Length | None = Field(
        validation_alias="torqueReferencePoint", serialization_alias="torqueReferencePoint", default=None
    )
