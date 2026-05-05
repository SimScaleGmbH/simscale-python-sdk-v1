from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.number_of_cells_per_direction import NumberOfCellsPerDirection


class CustomEmbeddedBoundaryMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_EBM_MESH_SIZING",
        description="Schema name: CustomEmbeddedBoundaryMeshSizing",
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
