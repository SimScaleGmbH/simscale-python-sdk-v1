from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.particle_trace_animation_output_settings import (
    ParticleTraceAnimationOutputSettings,
)
from simscale_sdk_v1.models.reporting.shape_animation_output_settings import ShapeAnimationOutputSettings
from simscale_sdk_v1.models.reporting.time_step_animation_output_settings import TimeStepAnimationOutputSettings

_ONE_OF_ANIMATION_OUTPUT_SETTINGS_VARIANTS: dict[str, type] = {
    "TIME_STEP": TimeStepAnimationOutputSettings,
    "PARTICLE_TRACE": ParticleTraceAnimationOutputSettings,
    "SHAPE": ShapeAnimationOutputSettings,
}

OneOfAnimationOutputSettings = Annotated[
    Union[TimeStepAnimationOutputSettings, ParticleTraceAnimationOutputSettings, ShapeAnimationOutputSettings],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_ANIMATION_OUTPUT_SETTINGS_VARIANTS,
        )
    ),
]
