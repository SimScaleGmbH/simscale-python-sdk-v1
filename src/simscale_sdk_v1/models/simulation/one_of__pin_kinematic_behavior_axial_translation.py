from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.flexible_axial_translation import FlexibleAxialTranslation
from simscale_sdk_v1.models.simulation.free_axial_translation import FreeAxialTranslation
from simscale_sdk_v1.models.simulation.rigid_axial_translation import RigidAxialTranslation

# Define the translation behavior between the connected entities along the virtual pin axisFree sliding - bodies may freely translate along the pin axisRigid - translation of the bodies in the pin axis direction is lockedWith axial spring - translation is controlled by an axial spring stiffness, allowing the deformation of the virtual pin itself to affect global deformations
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
