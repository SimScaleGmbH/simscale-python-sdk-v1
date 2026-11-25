from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticCfMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_CF_MESH_SIZING",
        description="Schema name: AutomaticCfMeshSizing",
    )
    fineness: float | None = Field(
        default=5.0,
        description="The fineness controls the overall mesh sizing from coarse (0) to fine (10). The maximum cell size is derived from the extent of the geometry and the size of its largest faces. Curvature, narrow gaps and small features are refined automatically, and this refinement gets deeper with a higher fineness. At fineness 0 the mesh is the coarsest mesh that still resolves the geometry; higher values refine it from there.A finer setting captures geometry details better but increases the cell count, the meshing time and the simulation cost. To refine the mesh locally, prefer surface and volume custom sizings over a higher global fineness.",
    )
