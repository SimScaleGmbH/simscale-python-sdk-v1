from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.predefined_rotational_motion import PredefinedRotationalMotion
from simscale_sdk_v1.models.simulation.predefined_translational_motion import PredefinedTranslationalMotion

_ONE_OF__ELECTROMAGNETIC_ADVANCED_CONCEPTS_MOTION_ANALYSIS_VARIANTS: dict[str, type] = {
    "PREDEFINED_ROTATIONAL_MOTION": PredefinedRotationalMotion,
    "PREDEFINED_TRANSLATIONAL_MOTION": PredefinedTranslationalMotion,
}

OneOf_ElectromagneticAdvancedConceptsMotionAnalysis = Annotated[
    Union[PredefinedRotationalMotion, PredefinedTranslationalMotion],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELECTROMAGNETIC_ADVANCED_CONCEPTS_MOTION_ANALYSIS_VARIANTS,
        )
    ),
]
