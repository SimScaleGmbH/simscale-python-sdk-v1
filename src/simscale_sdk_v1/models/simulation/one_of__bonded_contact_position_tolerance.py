from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.off_position_tolerance import OffPositionTolerance
from simscale_sdk_v1.models.simulation.set_value_position_tolerance import SetValuePositionTolerance

_ONE_OF__BONDED_CONTACT_POSITION_TOLERANCE_VARIANTS: dict[str, type] = {
    "SET_VALUE": SetValuePositionTolerance,
    "OFF": OffPositionTolerance,
}

OneOf_BondedContactPositionTolerance = Annotated[
    Union[SetValuePositionTolerance, OffPositionTolerance],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__BONDED_CONTACT_POSITION_TOLERANCE_VARIANTS,
        )
    ),
]
