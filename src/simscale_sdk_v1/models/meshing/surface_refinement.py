from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__surface_refinement_cell_zone import OneOf_SurfaceRefinementCellZone
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SurfaceRefinement(SimScaleModel):
    """A surface refinement can be used to refine the mesh near the surfaces of assigned faces and/or solids. A surface refinement can also be used to create a cell zone."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_V3",
        description="A surface refinement can be used to refine the mesh near the surfaces of assigned faces and/or solids. A surface refinement can also be used to create a cell zone.  Schema name: SurfaceRefinement",
    )
    name: str | None = Field(default="Surface refinement")
    min_level: int | None = Field(
        validation_alias="minLevel",
        serialization_alias="minLevel",
        default=1,
        description="Specify surface-wise the minimum refinement level for this surface.",
    )
    max_level: int | None = Field(
        validation_alias="maxLevel",
        serialization_alias="maxLevel",
        default=2,
        description="Specify surface-wise the maximum refinement level for this surface.",
    )
    cell_zone: OneOf_SurfaceRefinementCellZone | None = Field(
        validation_alias="cellZone", serialization_alias="cellZone", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
