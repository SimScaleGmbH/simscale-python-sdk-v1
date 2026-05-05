from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ClosedCoil(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CLOSED_COIL",
        description="Schema name: ClosedCoil",
    )
    bodies: TopologicalReference | None = Field(default=None)
    internal_port: TopologicalReference | None = Field(
        validation_alias="internalPort", serialization_alias="internalPort", default=None
    )
