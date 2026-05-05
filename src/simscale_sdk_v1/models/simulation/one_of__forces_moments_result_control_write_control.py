from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.coarse_resolution import CoarseResolution
from simscale_sdk_v1.models.simulation.custom_resolution import CustomResolution
from simscale_sdk_v1.models.simulation.high_resolution import HighResolution
from simscale_sdk_v1.models.simulation.moderate_resolution import ModerateResolution
from simscale_sdk_v1.models.simulation.synchronize_with_field_output_write_control import (
    SynchronizeWithFieldOutputWriteControl,
)
from simscale_sdk_v1.models.simulation.time_step_write_control import TimeStepWriteControl

_ONE_OF__FORCES_MOMENTS_RESULT_CONTROL_WRITE_CONTROL_VARIANTS: dict[str, type] = {
    "TIME_STEP": TimeStepWriteControl,
    "OUTPUT_TIME": SynchronizeWithFieldOutputWriteControl,
    "HIGH_RESOLUTION": HighResolution,
    "MODERATE_RESOLUTION": ModerateResolution,
    "COARSE_RESOLUTION": CoarseResolution,
    "CUSTOM_RESOLUTION": CustomResolution,
}

OneOf_ForcesMomentsResultControlWriteControl = Annotated[
    Union[
        TimeStepWriteControl,
        SynchronizeWithFieldOutputWriteControl,
        HighResolution,
        ModerateResolution,
        CoarseResolution,
        CustomResolution,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FORCES_MOMENTS_RESULT_CONTROL_WRITE_CONTROL_VARIANTS,
        )
    ),
]
