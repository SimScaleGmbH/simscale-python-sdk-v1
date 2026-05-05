from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.adjustable_runtime_write_control import AdjustableRuntimeWriteControl
from simscale_sdk_v1.models.simulation.clock_time_write_control import ClockTimeWriteControl
from simscale_sdk_v1.models.simulation.cpu_time_write_control import CpuTimeWriteControl
from simscale_sdk_v1.models.simulation.number_iterations_write_control import NumberIterationsWriteControl
from simscale_sdk_v1.models.simulation.run_time_write_control import RunTimeWriteControl
from simscale_sdk_v1.models.simulation.time_step_write_control import TimeStepWriteControl

_ONE_OF__FLUID_SIMULATION_CONTROL_WRITE_CONTROL_VARIANTS: dict[str, type] = {
    "TIME_STEP": TimeStepWriteControl,
    "CLOCK_TIME": ClockTimeWriteControl,
    "RUNTIME": RunTimeWriteControl,
    "CPU_TIME": CpuTimeWriteControl,
    "ADJUSTABLE_RUNTIME": AdjustableRuntimeWriteControl,
    "NUMBER_OF_ITERATIONS_STEADY_STATE": NumberIterationsWriteControl,
}

OneOf_FluidSimulationControlWriteControl = Annotated[
    Union[
        TimeStepWriteControl,
        ClockTimeWriteControl,
        RunTimeWriteControl,
        CpuTimeWriteControl,
        AdjustableRuntimeWriteControl,
        NumberIterationsWriteControl,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_SIMULATION_CONTROL_WRITE_CONTROL_VARIANTS,
        )
    ),
]
