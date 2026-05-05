from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.all_computed_write_control import AllComputedWriteControl
from simscale_sdk_v1.models.simulation.initial_timesteps_write_control import InitialTimestepsWriteControl
from simscale_sdk_v1.models.simulation.user_defined_write_control import UserDefinedWriteControl
from simscale_sdk_v1.models.simulation.write_interval_write_control import WriteIntervalWriteControl

_ONE_OF__SOLID_SIMULATION_CONTROL_WRITE_CONTROL_DEFINITION_VARIANTS: dict[str, type] = {
    "WRITE_INTERVAL": WriteIntervalWriteControl,
    "ALL_COMPUTED": AllComputedWriteControl,
    "INITIAL": InitialTimestepsWriteControl,
    "USER_DEFINED_V21": UserDefinedWriteControl,
}

OneOf_SolidSimulationControlWriteControlDefinition = Annotated[
    Union[WriteIntervalWriteControl, AllComputedWriteControl, InitialTimestepsWriteControl, UserDefinedWriteControl],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_SIMULATION_CONTROL_WRITE_CONTROL_DEFINITION_VARIANTS,
        )
    ),
]
