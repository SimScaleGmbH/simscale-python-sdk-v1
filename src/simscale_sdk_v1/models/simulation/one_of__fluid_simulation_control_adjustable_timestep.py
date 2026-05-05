from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.active_adjustable_timestep import ActiveAdjustableTimestep
from simscale_sdk_v1.models.simulation.inactive_adjustable_timestep import InactiveAdjustableTimestep

_ONE_OF__FLUID_SIMULATION_CONTROL_ADJUSTABLE_TIMESTEP_VARIANTS: dict[str, type] = {
    "INACTIVE_TIMESTEP": InactiveAdjustableTimestep,
    "ACTIVE_TIMESTEP": ActiveAdjustableTimestep,
}

OneOf_FluidSimulationControlAdjustableTimestep = Annotated[
    Union[InactiveAdjustableTimestep, ActiveAdjustableTimestep],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_SIMULATION_CONTROL_ADJUSTABLE_TIMESTEP_VARIANTS,
        )
    ),
]
