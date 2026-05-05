from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__new_surface_refinement_pacefish_v38_mesh_sizing import (
    OneOf_NewSurfaceRefinementPacefishV38MeshSizing,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class NewSurfaceRefinementPacefishV38(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_PACEFISH_V38",
        description="Schema name: NewSurfaceRefinementPacefishV38",
    )
    name: str | None = Field(default="Surface refinement")
    mesh_sizing: OneOf_NewSurfaceRefinementPacefishV38MeshSizing | None = Field(
        validation_alias="meshSizing", serialization_alias="meshSizing", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
