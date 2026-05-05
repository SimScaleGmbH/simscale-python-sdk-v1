from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_harmonic_displacement_type import AbsoluteHarmonicDisplacementType
from simscale_sdk_v1.models.simulation.relative_harmonic_displacement_type import RelativeHarmonicDisplacementType

_ONE_OF__HARMONIC_DISPLACEMENT_RESULT_CONTROL_ITEM_HARMONIC_DISPLACEMENT_TYPE_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsoluteHarmonicDisplacementType,
    "RELATIVE": RelativeHarmonicDisplacementType,
}

OneOf_HarmonicDisplacementResultControlItemHarmonicDisplacementType = Annotated[
    Union[AbsoluteHarmonicDisplacementType, RelativeHarmonicDisplacementType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HARMONIC_DISPLACEMENT_RESULT_CONTROL_ITEM_HARMONIC_DISPLACEMENT_TYPE_VARIANTS,
        )
    ),
]
