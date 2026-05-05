from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.oscillating_rotating_motion_type import OscillatingRotatingMotionType
from simscale_sdk_v1.models.simulation.rotating_motion_type import RotatingMotionType

_ONE_OF_AMI_ROTATING_ZONE_MOTION_TYPE_VARIANTS: dict[str, type] = {
    "OSCILLATING_ROTATING_MOTION": OscillatingRotatingMotionType,
    "ROTATING_MOTION": RotatingMotionType,
}

OneOf_AMIRotatingZoneMotionType = Annotated[
    Union[OscillatingRotatingMotionType, RotatingMotionType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_AMI_ROTATING_ZONE_MOTION_TYPE_VARIANTS,
        )
    ),
]
