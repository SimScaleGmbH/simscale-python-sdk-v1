from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.round import Round
from simscale_sdk_v1.models.simulation.square import Square

_ONE_OF__LITZ_WIRE_COIL_STRAND_CROSS_SECTION_TYPE_VARIANTS: dict[str, type] = {
    "ROUND": Round,
    "SQUARE": Square,
}

OneOf_LitzWireCoilStrandCrossSectionType = Annotated[
    Union[Round, Square],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__LITZ_WIRE_COIL_STRAND_CROSS_SECTION_TYPE_VARIANTS,
        )
    ),
]
