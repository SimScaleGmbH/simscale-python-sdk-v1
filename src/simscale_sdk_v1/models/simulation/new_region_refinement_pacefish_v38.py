from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__new_region_refinement_pacefish_v38_mesh_sizing import (
    OneOf_NewRegionRefinementPacefishV38MeshSizing,
)


class NewRegionRefinementPacefishV38(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_PACEFISH_V38",
        description="Schema name: NewRegionRefinementPacefishV38",
    )
    name: str | None = Field(default="Region refinement")
    mesh_sizing: OneOf_NewRegionRefinementPacefishV38MeshSizing | None = Field(
        validation_alias="meshSizing", serialization_alias="meshSizing", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
