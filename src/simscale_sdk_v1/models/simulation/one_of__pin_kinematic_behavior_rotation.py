from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.free_axial_rotation import FreeAxialRotation
from simscale_sdk_v1.models.simulation.rigid_axial_rotation import RigidAxialRotation
from simscale_sdk_v1.models.simulation.torsional_axial_rotation import TorsionalAxialRotation

# Rotation about the pin axis, between the parts (Body to body) or against the ground (Body to ground):Free rotation: the parts turn freely, like a hinge.Rigid: rotation is locked.With torsion spring: the Torsion spring stiffness resists the rotation.Note: with Free rotation, a part that is held only by this pin can spin about it, and the solver stops with a singular matrix. Hold the part elsewhere too (a second pin, a contact or a support), or use a soft torsion spring.
_ONE_OF__PIN_KINEMATIC_BEHAVIOR_ROTATION_VARIANTS: dict[str, type] = {
    "FREE": FreeAxialRotation,
    "RIGID": RigidAxialRotation,
    "TORSIONAL": TorsionalAxialRotation,
}

OneOf_PinKinematicBehaviorRotation = Annotated[
    Union[FreeAxialRotation, RigidAxialRotation, TorsionalAxialRotation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PIN_KINEMATIC_BEHAVIOR_ROTATION_VARIANTS,
        )
    ),
]
