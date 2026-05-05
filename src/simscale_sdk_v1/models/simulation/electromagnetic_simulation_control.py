from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.electromagnetic_transient_control import ElectromagneticTransientControl
from simscale_sdk_v1.models.simulation.time_step_write_control import TimeStepWriteControl


class ElectromagneticSimulationControl(SimScaleModel):
    transient_magnetics_control: ElectromagneticTransientControl | None = Field(
        validation_alias="transientMagneticsControl", serialization_alias="transientMagneticsControl", default=None
    )
    write_control: TimeStepWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    num_processors: Literal[-1, 1, 2, 4, 8, 16, 32, 48, 64, 96, 128, 192] | None = Field(
        validation_alias="numProcessors",
        serialization_alias="numProcessors",
        default=-1,
        description="Selecting more processor cores will speed up the simulation process. Choosing a smaller computation instance will save core hours. Learn more.",
    )
    max_run_time: Dimensional_Time | None = Field(
        validation_alias="maxRunTime", serialization_alias="maxRunTime", default=None
    )
    core_loss_reference_period: Dimensional_Time | None = Field(
        validation_alias="coreLossReferencePeriod", serialization_alias="coreLossReferencePeriod", default=None
    )
    time_periodic_acceleration: bool | None = Field(
        validation_alias="timePeriodicAcceleration",
        serialization_alias="timePeriodicAcceleration",
        default=False,
        description="Activate when the coil excitation is periodic to accelerate simulation. For more information, please refer to our documentation.",
    )
