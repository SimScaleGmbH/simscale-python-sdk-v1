from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PeriodicBC(SimScaleModel):
    """This boundary condition should be used on two faces of a system as if they are physically connected. It is required that the two faces are of same size and shape and the face elements of the mesh are congruent on both sides. Works for uploaded meshes only. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PERIODIC",
        description="This boundary condition should be used on two faces of a system as if they are physically connected. It is required that the two faces are of same size and shape and the face elements of the mesh are congruent on both sides. Works for uploaded meshes only. Learn more.  Schema name: PeriodicBC",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
