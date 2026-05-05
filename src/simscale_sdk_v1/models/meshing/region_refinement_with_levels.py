from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__region_refinement_with_levels_refinement import (
    OneOf_RegionRefinementWithLevelsRefinement,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class RegionRefinementWithLevels(SimScaleModel):
    """A region refinement can be used to refine the mesh in a given area. The refinement area needs to be defined either via a geometry primitive or an existing solid (Hex-dominant only)."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_LEVELS",
        description="A region refinement can be used to refine the mesh in a given area. The refinement area needs to be defined either via a geometry primitive or an existing solid (Hex-dominant only).  Schema name: RegionRefinementWithLevels",
    )
    name: str | None = Field(default="Region refinement")
    refinement: OneOf_RegionRefinementWithLevelsRefinement | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
