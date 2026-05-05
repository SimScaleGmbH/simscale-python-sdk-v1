from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.number_of_cells_per_direction import NumberOfCellsPerDirection


class CustomPolygridMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_POLYGRID_MESH_SIZING",
        description="Schema name: CustomPolygridMeshSizing",
    )
    num_cells_per_direction: NumberOfCellsPerDirection | None = Field(
        validation_alias="numCellsPerDirection", serialization_alias="numCellsPerDirection", default=None
    )
    num_refinement_levels: int | None = Field(
        validation_alias="numRefinementLevels",
        serialization_alias="numRefinementLevels",
        default=3,
        description="Number of refinement levels to refine in the vicinity of all CAD surfaces.",
    )
    physics_based_meshing_ibm: bool | None = Field(
        validation_alias="physicsBasedMeshingIBM",
        serialization_alias="physicsBasedMeshingIBM",
        default=True,
        description="Physics-based meshing takes setup information into account to size the immersed mesh accordingly. Users can expect automatic refinements applied to the following: Boundary faces: All of those which belong to a boundary condition. Advanced concepts: Power and momentum sources, porous regions and thermal resistance networks.",
    )
