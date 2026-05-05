from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.marc_output_writing_container import MarcOutputWritingContainer
from simscale_sdk_v1.models.simulation.one_of__marc_simulation_control_timestep_definition import (
    OneOf_MarcSimulationControlTimestepDefinition,
)


class MarcSimulationControl(SimScaleModel):
    timestep_definition: OneOf_MarcSimulationControlTimestepDefinition | None = Field(
        validation_alias="timestepDefinition", serialization_alias="timestepDefinition", default=None
    )
    output_writing_container: MarcOutputWritingContainer | None = Field(
        validation_alias="outputWritingContainer", serialization_alias="outputWritingContainer", default=None
    )
    num_processors: Literal[-1, 1, 2, 4, 8, 16, 32, 48, 64, 96, 128, 192] | None = Field(
        validation_alias="numProcessors",
        serialization_alias="numProcessors",
        default=-1,
        description="Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    manually_assign_parallelization: bool | None = Field(
        validation_alias="manuallyAssignParallelization",
        serialization_alias="manuallyAssignParallelization",
        default=False,
    )
    nprocds: int | None = Field(default=-1)
    nte: int | None = Field(default=-1)
    nts: int | None = Field(default=-1)
    nsolver: int | None = Field(default=-1)
    max_run_time: Dimensional_Time | None = Field(
        validation_alias="maxRunTime", serialization_alias="maxRunTime", default=None
    )
    live_postprocessing: bool | None = Field(
        validation_alias="livePostprocessing",
        serialization_alias="livePostprocessing",
        default=True,
        description="Determines whether simulation results are updated in the post-processor in real-time while the solver is still running. Enabling this allows for early inspection of the structural behavior before the full analysis completes. This option is particularly useful for long running simulations.",
    )
