from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class WedgeBC(SimScaleModel):
    """This boundary condition is applied to the front and back faces of an axisymmetric system (eg. cylinder). Note that the face elements of the mesh need to be congruent on both the faces. Works for uploaded 2D meshes only.  Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WEDGE",
        description="This boundary condition is applied to the front and back faces of an axisymmetric system (eg. cylinder). Note that the face elements of the mesh need to be congruent on both the faces. Works for uploaded 2D meshes only.  Learn more.  Schema name: WedgeBC",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
