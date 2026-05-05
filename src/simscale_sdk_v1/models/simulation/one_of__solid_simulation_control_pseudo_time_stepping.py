from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.single_step_pseudo_time_stepping import SingleStepPseudoTimeStepping
from simscale_sdk_v1.models.simulation.stepping_list_pseudo_time_stepping import SteppingListPseudoTimeStepping

_ONE_OF__SOLID_SIMULATION_CONTROL_PSEUDO_TIME_STEPPING_VARIANTS: dict[str, type] = {
    "SINGLE_STEP": SingleStepPseudoTimeStepping,
    "STEPPING_LIST_V18": SteppingListPseudoTimeStepping,
}

OneOf_SolidSimulationControlPseudoTimeStepping = Annotated[
    Union[SingleStepPseudoTimeStepping, SteppingListPseudoTimeStepping],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_SIMULATION_CONTROL_PSEUDO_TIME_STEPPING_VARIANTS,
        )
    ),
]
