from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class TestsolverSimulationControl(SimScaleModel):
    num_processors: Literal[-1, 1, 2, 4, 8, 16, 32, 48, 64, 96, 128, 192] | None = Field(
        validation_alias="numProcessors",
        serialization_alias="numProcessors",
        default=-1,
        description="Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    max_run_time: Dimensional_Time | None = Field(
        validation_alias="maxRunTime", serialization_alias="maxRunTime", default=None
    )
    execution_mode: str | None = Field(
        validation_alias="executionMode", serialization_alias="executionMode", default="SUCCESS"
    )
    execution_mode_config: str | None = Field(
        validation_alias="executionModeConfig", serialization_alias="executionModeConfig", default="{}"
    )
