from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_meshing_refinements import (
    OneOf_EmbeddedBoundaryMeshingRefinements,
)
from simscale_sdk_v1.models.simulation.one_of__embedded_boundary_meshing_sizing import (
    OneOf_EmbeddedBoundaryMeshingSizing,
)


class EmbeddedBoundaryMeshing(SimScaleModel):
    sizing: OneOf_EmbeddedBoundaryMeshingSizing | None = Field(default=None)
    number_of_buffer_cells: float | None = Field(
        validation_alias="numberOfBufferCells",
        serialization_alias="numberOfBufferCells",
        default=4.0,
        description="Target number of cells for every cell size level. Higher number of buffer cells ensure smoother cell size transitions, which results in better accuracy but bigger computation costs. On the other hand, lower number of buffer cells will result in smaller computation costs but worse accuracy.",
    )
    refinements: list[OneOf_EmbeddedBoundaryMeshingRefinements] | None = Field(default=None)
