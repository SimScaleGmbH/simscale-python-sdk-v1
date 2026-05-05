from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.manual_timestep_calculation_type import ManualTimestepCalculationType
from simscale_sdk_v1.models.simulation.newton_iteration_timestep_calculation_type import (
    NewtonIterationTimestepCalculationType,
)

_ONE_OF__ERROR_RETIMING_EVENT_TIMESTEP_CALCULATION_TYPE_VARIANTS: dict[str, type] = {
    "NEWTON_ITERATION": NewtonIterationTimestepCalculationType,
    "MANUAL": ManualTimestepCalculationType,
}

OneOf_ErrorRetimingEventTimestepCalculationType = Annotated[
    Union[NewtonIterationTimestepCalculationType, ManualTimestepCalculationType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ERROR_RETIMING_EVENT_TIMESTEP_CALCULATION_TYPE_VARIANTS,
        )
    ),
]
