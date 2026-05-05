from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.free_axial_rotation import FreeAxialRotation
from simscale_sdk_v1.models.simulation.rigid_axial_rotation import RigidAxialRotation
from simscale_sdk_v1.models.simulation.torsional_axial_rotation import TorsionalAxialRotation

# Define the rotational behavior between the connected entitiesFree rotation - bodies may freely rotate about the pin axisRigid - rotation of the bodies about the pin axis direction is lockedWith torsion spring - rotation is controlled by a torsion spring stiffness
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
