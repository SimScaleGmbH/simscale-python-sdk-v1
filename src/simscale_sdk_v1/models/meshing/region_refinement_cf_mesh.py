from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.inside_region_refinement_with_length import InsideRegionRefinementWithLength


class RegionRefinementCfMesh(SimScaleModel):
    """Volume custom sizing refines all cells inside the assigned geometry primitives (cartesian box, cylinder or sphere) or solid CAD bodies to the given maximum edge length. Use it to refine regions of interest away from surfaces, for example wakes or jets. The refinement always applies to the inside of the assigned primitives and bodies. An assigned body must also be the meshed region itself (with physics-based meshing, the volume with the material assignment), a cell zone or, with physics-based meshing, a volume assigned to an advanced concept such as a rotating zone or porous medium."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_REFINEMENT_CF_MESH",
        description="Volume custom sizing refines all cells inside the assigned geometry primitives (cartesian box, cylinder or sphere) or solid CAD bodies to the given maximum edge length. Use it to refine regions of interest away from surfaces, for example wakes or jets. The refinement always applies to the inside of the assigned primitives and bodies. An assigned body must also be the meshed region itself (with physics-based meshing, the volume with the material assignment), a cell zone or, with physics-based meshing, a volume assigned to an advanced concept such as a rotating zone or porous medium.  Schema name: RegionRefinementCfMesh",
    )
    name: str | None = Field(default=None)
    refinement: InsideRegionRefinementWithLength | None = Field(default=None)
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
