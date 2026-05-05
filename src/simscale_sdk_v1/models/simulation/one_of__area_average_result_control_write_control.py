from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.number_iterations_write_control import NumberIterationsWriteControl
from simscale_sdk_v1.models.simulation.synchronize_with_field_output_write_control import (
    SynchronizeWithFieldOutputWriteControl,
)
from simscale_sdk_v1.models.simulation.time_step_write_control import TimeStepWriteControl

_ONE_OF__AREA_AVERAGE_RESULT_CONTROL_WRITE_CONTROL_VARIANTS: dict[str, type] = {
    "TIME_STEP": TimeStepWriteControl,
    "OUTPUT_TIME": SynchronizeWithFieldOutputWriteControl,
    "NUMBER_OF_ITERATIONS_STEADY_STATE": NumberIterationsWriteControl,
}

OneOf_AreaAverageResultControlWriteControl = Annotated[
    Union[TimeStepWriteControl, SynchronizeWithFieldOutputWriteControl, NumberIterationsWriteControl],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__AREA_AVERAGE_RESULT_CONTROL_WRITE_CONTROL_VARIANTS,
        )
    ),
]
