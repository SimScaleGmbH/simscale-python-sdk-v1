from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_harmonic_acceleration_type import AbsoluteHarmonicAccelerationType
from simscale_sdk_v1.models.simulation.relative_harmonic_acceleration_type import RelativeHarmonicAccelerationType

_ONE_OF__HARMONIC_ACCELERATION_RESULT_CONTROL_ITEM_HARMONIC_ACCELERATION_TYPE_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsoluteHarmonicAccelerationType,
    "RELATIVE": RelativeHarmonicAccelerationType,
}

OneOf_HarmonicAccelerationResultControlItemHarmonicAccelerationType = Annotated[
    Union[AbsoluteHarmonicAccelerationType, RelativeHarmonicAccelerationType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HARMONIC_ACCELERATION_RESULT_CONTROL_ITEM_HARMONIC_ACCELERATION_TYPE_VARIANTS,
        )
    ),
]
