from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__region_refinement_with_length_curvature import (
    OneOf_RegionRefinementWithLengthCurvature,
)
from simscale_sdk_v1.models.meshing.one_of__region_refinement_with_length_refinement import (
    OneOf_RegionRefinementWithLengthRefinement,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class RegionRefinementWithLength(SimScaleModel):
    """A region refinement can be used to refine the mesh in a given area. The refinement area needs to be defined either via an existing solid or a geometry primitive."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_LENGTH",
        description="A region refinement can be used to refine the mesh in a given area. The refinement area needs to be defined either via an existing solid or a geometry primitive.  Schema name: RegionRefinementWithLength",
    )
    name: str | None = Field(default="Region refinement")
    refinement: OneOf_RegionRefinementWithLengthRefinement | None = Field(default=None)
    curvature: OneOf_RegionRefinementWithLengthCurvature | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
