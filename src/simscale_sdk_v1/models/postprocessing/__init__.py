"""Generated Postprocessing models — lazy-loaded."""

from __future__ import annotations

import importlib

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from simscale_sdk_v1.models.postprocessing.one_of_state_animation_output_settings import (
        OneOfStateAnimationOutputSettings,
    )
    from simscale_sdk_v1.models.postprocessing.state_animation_output_settings import StateAnimationOutputSettings
    from simscale_sdk_v1.models.postprocessing.state_particle_trace_animation_output_settings import (
        StateParticleTraceAnimationOutputSettings,
    )
    from simscale_sdk_v1.models.postprocessing.state_response import StateResponse
    from simscale_sdk_v1.models.postprocessing.state_screenshot_output_settings import StateScreenshotOutputSettings
    from simscale_sdk_v1.models.postprocessing.state_shape_animation_output_settings import (
        StateShapeAnimationOutputSettings,
    )
    from simscale_sdk_v1.models.postprocessing.state_time_step_animation_output_settings import (
        StateTimeStepAnimationOutputSettings,
    )

_NAMES: dict[str, tuple[str, str]] = {
    "OneOfStateAnimationOutputSettings": (
        "simscale_sdk_v1.models.postprocessing.one_of_state_animation_output_settings",
        "OneOfStateAnimationOutputSettings",
    ),
    "StateAnimationOutputSettings": (
        "simscale_sdk_v1.models.postprocessing.state_animation_output_settings",
        "StateAnimationOutputSettings",
    ),
    "StateParticleTraceAnimationOutputSettings": (
        "simscale_sdk_v1.models.postprocessing.state_particle_trace_animation_output_settings",
        "StateParticleTraceAnimationOutputSettings",
    ),
    "StateResponse": ("simscale_sdk_v1.models.postprocessing.state_response", "StateResponse"),
    "StateScreenshotOutputSettings": (
        "simscale_sdk_v1.models.postprocessing.state_screenshot_output_settings",
        "StateScreenshotOutputSettings",
    ),
    "StateShapeAnimationOutputSettings": (
        "simscale_sdk_v1.models.postprocessing.state_shape_animation_output_settings",
        "StateShapeAnimationOutputSettings",
    ),
    "StateTimeStepAnimationOutputSettings": (
        "simscale_sdk_v1.models.postprocessing.state_time_step_animation_output_settings",
        "StateTimeStepAnimationOutputSettings",
    ),
}


def __getattr__(name: str):
    if name in _NAMES:
        module_path, attr_name = _NAMES[name]
        module = importlib.import_module(module_path)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_NAMES.keys())
