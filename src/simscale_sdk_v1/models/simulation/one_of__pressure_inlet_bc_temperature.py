from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_value_tbc import FixedValueTBC
from simscale_sdk_v1.models.simulation.total_tbc import TotalTBC

# Please choose a boundary condition for temperature (T).
_ONE_OF__PRESSURE_INLET_BC_TEMPERATURE_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValueTBC,
    "TOTAL_TEMPERATURE": TotalTBC,
}

OneOf_PressureInletBCTemperature = Annotated[
    Union[FixedValueTBC, TotalTBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRESSURE_INLET_BC_TEMPERATURE_VARIANTS,
        )
    ),
]
