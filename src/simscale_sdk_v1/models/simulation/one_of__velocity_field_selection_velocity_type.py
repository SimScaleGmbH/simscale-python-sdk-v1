from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_harmonic_velocity_field_type import AbsoluteHarmonicVelocityFieldType
from simscale_sdk_v1.models.simulation.relative_harmonic_velocity_field_type import RelativeHarmonicVelocityFieldType

_ONE_OF__VELOCITY_FIELD_SELECTION_VELOCITY_TYPE_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsoluteHarmonicVelocityFieldType,
    "RELATIVE": RelativeHarmonicVelocityFieldType,
}

OneOf_VelocityFieldSelectionVelocityType = Annotated[
    Union[AbsoluteHarmonicVelocityFieldType, RelativeHarmonicVelocityFieldType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_FIELD_SELECTION_VELOCITY_TYPE_VARIANTS,
        )
    ),
]
