from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticPolygridMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_POLYGRID_MESH_SIZING",
        description="Schema name: AutomaticPolygridMeshSizing",
    )
    fineness: float | None = Field(
        default=5.0,
        description="This parameter determines the fineness of the mesh and affects the overall number of cells.Note: This setting will impact the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results.",
    )
    physics_based_meshing_ibm: bool | None = Field(
        validation_alias="physicsBasedMeshingIBM",
        serialization_alias="physicsBasedMeshingIBM",
        default=True,
        description="Physics-based meshing takes setup information into account to size the immersed mesh accordingly. Users can expect automatic refinements applied to the following: Boundary faces: All of those which belong to a boundary condition. Advanced concepts: Power and momentum sources, porous regions and thermal resistance networks.",
    )
