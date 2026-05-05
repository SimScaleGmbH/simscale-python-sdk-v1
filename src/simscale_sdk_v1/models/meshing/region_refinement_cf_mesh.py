from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.inside_region_refinement_with_length import InsideRegionRefinementWithLength


class RegionRefinementCfMesh(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_REFINEMENT_CF_MESH",
        description="Schema name: RegionRefinementCfMesh",
    )
    name: str | None = Field(default=None)
    refinement: InsideRegionRefinementWithLength | None = Field(default=None)
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
