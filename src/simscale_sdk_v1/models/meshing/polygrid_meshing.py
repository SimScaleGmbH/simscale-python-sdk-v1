from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.meshing.one_of__polygrid_meshing_refinements import OneOf_PolygridMeshingRefinements
from simscale_sdk_v1.models.meshing.one_of__polygrid_meshing_sizing import OneOf_PolygridMeshingSizing


class PolygridMeshing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POLYGRID_MESHING",
        description="Schema name: PolygridMeshing",
    )
    sizing: OneOf_PolygridMeshingSizing | None = Field(default=None)
    refinements: list[OneOf_PolygridMeshingRefinements] | None = Field(default=None)
    number_of_buffer_cells: float | None = Field(
        validation_alias="numberOfBufferCells",
        serialization_alias="numberOfBufferCells",
        default=4.0,
        description="Target number of cells for every cell size level. Higher number of buffer cells ensure smoother cell size transitions, which results in better accuracy but bigger computation costs. On the other hand, lower number of buffer cells will result in smaller computation costs but worse accuracy.",
    )
    num_of_processors: Literal[-1, 4, 8, 16, 32, 64, 96] | None = Field(
        validation_alias="numOfProcessors",
        serialization_alias="numOfProcessors",
        default=-1,
        description="Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    max_meshing_run_time: Dimensional_Time | None = Field(
        validation_alias="maxMeshingRunTime", serialization_alias="maxMeshingRunTime", default=None
    )
