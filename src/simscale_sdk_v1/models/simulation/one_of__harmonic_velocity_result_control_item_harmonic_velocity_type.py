from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_harmonic_velocity_type import AbsoluteHarmonicVelocityType
from simscale_sdk_v1.models.simulation.relative_harmonic_velocity_type import RelativeHarmonicVelocityType

_ONE_OF__HARMONIC_VELOCITY_RESULT_CONTROL_ITEM_HARMONIC_VELOCITY_TYPE_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsoluteHarmonicVelocityType,
    "RELATIVE": RelativeHarmonicVelocityType,
}

OneOf_HarmonicVelocityResultControlItemHarmonicVelocityType = Annotated[
    Union[AbsoluteHarmonicVelocityType, RelativeHarmonicVelocityType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HARMONIC_VELOCITY_RESULT_CONTROL_ITEM_HARMONIC_VELOCITY_TYPE_VARIANTS,
        )
    ),
]
