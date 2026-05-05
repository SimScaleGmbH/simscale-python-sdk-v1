from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_harmonic_displacement_field_type import (
    AbsoluteHarmonicDisplacementFieldType,
)
from simscale_sdk_v1.models.simulation.relative_harmonic_displacement_field_type import (
    RelativeHarmonicDisplacementFieldType,
)

_ONE_OF__DISPLACEMENT_FIELD_SELECTION_DISPLACEMENT_TYPE_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsoluteHarmonicDisplacementFieldType,
    "RELATIVE": RelativeHarmonicDisplacementFieldType,
}

OneOf_DisplacementFieldSelectionDisplacementType = Annotated[
    Union[AbsoluteHarmonicDisplacementFieldType, RelativeHarmonicDisplacementFieldType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DISPLACEMENT_FIELD_SELECTION_DISPLACEMENT_TYPE_VARIANTS,
        )
    ),
]
