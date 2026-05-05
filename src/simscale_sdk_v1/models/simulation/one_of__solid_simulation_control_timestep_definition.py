from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.auto_timestep_definition import AutoTimestepDefinition
from simscale_sdk_v1.models.simulation.manual_timestep_definition import ManualTimestepDefinition

_ONE_OF__SOLID_SIMULATION_CONTROL_TIMESTEP_DEFINITION_VARIANTS: dict[str, type] = {
    "AUTOMATIC_V27": AutoTimestepDefinition,
    "MANUAL_V19": ManualTimestepDefinition,
}

OneOf_SolidSimulationControlTimestepDefinition = Annotated[
    Union[AutoTimestepDefinition, ManualTimestepDefinition],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_SIMULATION_CONTROL_TIMESTEP_DEFINITION_VARIANTS,
        )
    ),
]
