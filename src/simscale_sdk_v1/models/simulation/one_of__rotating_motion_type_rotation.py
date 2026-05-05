from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.angular_rotation import AngularRotation
from simscale_sdk_v1.models.simulation.vector_rotation import VectorRotation

_ONE_OF__ROTATING_MOTION_TYPE_ROTATION_VARIANTS: dict[str, type] = {
    "ANGULAR_ROTATION": AngularRotation,
    "VECTOR_ROTATION": VectorRotation,
}

OneOf_RotatingMotionTypeRotation = Annotated[
    Union[AngularRotation, VectorRotation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ROTATING_MOTION_TYPE_ROTATION_VARIANTS,
        )
    ),
]
