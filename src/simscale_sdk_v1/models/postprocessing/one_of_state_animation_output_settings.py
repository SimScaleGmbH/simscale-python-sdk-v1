from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.postprocessing.state_particle_trace_animation_output_settings import (
    StateParticleTraceAnimationOutputSettings,
)
from simscale_sdk_v1.models.postprocessing.state_shape_animation_output_settings import (
    StateShapeAnimationOutputSettings,
)
from simscale_sdk_v1.models.postprocessing.state_time_step_animation_output_settings import (
    StateTimeStepAnimationOutputSettings,
)

_ONE_OF_STATE_ANIMATION_OUTPUT_SETTINGS_VARIANTS: dict[str, type] = {
    "TIME_STEP": StateTimeStepAnimationOutputSettings,
    "PARTICLE_TRACE": StateParticleTraceAnimationOutputSettings,
    "SHAPE": StateShapeAnimationOutputSettings,
}

OneOfStateAnimationOutputSettings = Annotated[
    Union[
        StateTimeStepAnimationOutputSettings,
        StateParticleTraceAnimationOutputSettings,
        StateShapeAnimationOutputSettings,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_STATE_ANIMATION_OUTPUT_SETTINGS_VARIANTS,
        )
    ),
]
