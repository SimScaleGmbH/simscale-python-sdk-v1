from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.force_moment_coefficients_result_control import (
    ForceMomentCoefficientsResultControl,
)
from simscale_sdk_v1.models.simulation.forces_moments_result_control import ForcesMomentsResultControl

_ONE_OF__FLUID_RESULT_CONTROLS_FORCES_MOMENTS_VARIANTS: dict[str, type] = {
    "FORCES_AND_MOMENTS": ForcesMomentsResultControl,
    "FORCE_AND_MOMENT_COEFFICIENTS": ForceMomentCoefficientsResultControl,
}

OneOf_FluidResultControlsForcesMoments = Annotated[
    Union[ForcesMomentsResultControl, ForceMomentCoefficientsResultControl],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_RESULT_CONTROLS_FORCES_MOMENTS_VARIANTS,
        )
    ),
]
