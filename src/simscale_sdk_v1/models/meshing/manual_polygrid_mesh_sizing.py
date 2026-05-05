from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class ManualPolygridMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_POLYGRID_MESH_SIZING",
        description="Schema name: ManualPolygridMeshSizing",
    )
    maximum_edge_length: Dimensional_Length | None = Field(
        validation_alias="maximumEdgeLength", serialization_alias="maximumEdgeLength", default=None
    )
    minimum_edge_length: Dimensional_Length | None = Field(
        validation_alias="minimumEdgeLength", serialization_alias="minimumEdgeLength", default=None
    )
    physics_based_meshing_ibm: bool | None = Field(
        validation_alias="physicsBasedMeshingIBM",
        serialization_alias="physicsBasedMeshingIBM",
        default=True,
        description="Physics-based meshing takes setup information into account to size the immersed mesh accordingly. Users can expect automatic refinements applied to the following: Boundary faces: All of those which belong to a boundary condition. Advanced concepts: Power and momentum sources, porous regions and thermal resistance networks.",
    )
