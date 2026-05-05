from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GAMGSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="GAMG", description="Schema name: GAMGSolver"
    )
    absolute_tolerance: float | None = Field(
        validation_alias="absoluteTolerance",
        serialization_alias="absoluteTolerance",
        default=None,
        description="Define the absolute tolerance for the residual. The convergence process will be stopped as soon as the residual falls below the absolute tolerance.",
    )
    relative_tolerance: float | None = Field(
        validation_alias="relativeTolerance",
        serialization_alias="relativeTolerance",
        default=None,
        description="Choose the relative tolerance for the residual. The convergence process will be stopped as soon as the ratio of current to initial residual falls below the relative tolerance.",
    )
    smoother: Literal["GAUSSSEIDEL", "DIC"] | None = Field(
        default=None, description="Choose a smoother for your solver."
    )
    num_pre_sweeps: int | None = Field(
        validation_alias="numPreSweeps", serialization_alias="numPreSweeps", default=None
    )
    num_post_sweeps: int | None = Field(
        validation_alias="numPostSweeps", serialization_alias="numPostSweeps", default=1
    )
    cache_agglomeration_on: bool | None = Field(
        validation_alias="cacheAgglomerationOn", serialization_alias="cacheAgglomerationOn", default=True
    )
    num_cells_coarsest_level: int | None = Field(
        validation_alias="numCellsCoarsestLevel", serialization_alias="numCellsCoarsestLevel", default=100
    )
    num_merge_levels: int | None = Field(
        validation_alias="numMergeLevels", serialization_alias="numMergeLevels", default=1
    )
