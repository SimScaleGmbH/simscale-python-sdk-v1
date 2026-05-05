from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__region_refinement_ebm_refinement import OneOf_RegionRefinementEBMRefinement
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class RegionRefinementEBM(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_REFINEMENT_EBM",
        description="Schema name: RegionRefinementEBM",
    )
    name: str | None = Field(default=None)
    refinement: OneOf_RegionRefinementEBMRefinement | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
