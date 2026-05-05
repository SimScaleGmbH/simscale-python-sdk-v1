from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class Empty2DBC(SimScaleModel):
    """This boundary condition is intended only for uploaded 2D OpenFOAM meshes. A 2D mesh is ensured by having a single cell thickness in one of the 3 spatial directions. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="EMPTY_2D",
        description="This boundary condition is intended only for uploaded 2D OpenFOAM meshes. A 2D mesh is ensured by having a single cell thickness in one of the 3 spatial directions. Learn more.  Schema name: Empty2DBC",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
