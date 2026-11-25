from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.flexible_axial_translation import FlexibleAxialTranslation
from simscale_sdk_v1.models.simulation.free_axial_translation import FreeAxialTranslation
from simscale_sdk_v1.models.simulation.rigid_axial_translation import RigidAxialTranslation

# Movement along the pin axis, between the parts (Body to body) or against the ground (Body to ground):Free sliding: the parts slide freely along the pin.Rigid: sliding is locked.With axial spring: the Axial spring stiffness resists the sliding.Note: with Free sliding, a part that is held only by this pin can move along the axis, and the solver stops with a singular matrix. A contact alone often does not hold it. Hold the part elsewhere, or use a soft axial spring (e.g. 10 N/m).
_ONE_OF__PIN_KINEMATIC_BEHAVIOR_AXIAL_TRANSLATION_VARIANTS: dict[str, type] = {
    "FREE": FreeAxialTranslation,
    "RIGID": RigidAxialTranslation,
    "FLEXIBLE": FlexibleAxialTranslation,
}

OneOf_PinKinematicBehaviorAxialTranslation = Annotated[
    Union[FreeAxialTranslation, RigidAxialTranslation, FlexibleAxialTranslation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PIN_KINEMATIC_BEHAVIOR_AXIAL_TRANSLATION_VARIANTS,
        )
    ),
]
