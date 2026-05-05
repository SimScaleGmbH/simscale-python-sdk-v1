from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.ambient_tbc import AmbientTBC
from simscale_sdk_v1.models.simulation.fixed_value_tbc import FixedValueTBC

# Please choose a boundary condition for temperature (T).
_ONE_OF__FAN_BC_TEMPERATURE_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValueTBC,
    "AMBIENT_TEMPERATURE": AmbientTBC,
}

OneOf_FanBCTemperature = Annotated[
    Union[FixedValueTBC, AmbientTBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FAN_BC_TEMPERATURE_VARIANTS,
        )
    ),
]
