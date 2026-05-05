from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.static_pressure_pressure_type import StaticPressurePressureType
from simscale_sdk_v1.models.simulation.total_pressure_pressure_type import TotalPressurePressureType

_ONE_OF__FIELD_CALCULATIONS_PRESSURE_RESULT_CONTROL_PRESSURE_TYPE_VARIANTS: dict[str, type] = {
    "TOTAL_PRESSURE": TotalPressurePressureType,
    "STATIC_PRESSURE": StaticPressurePressureType,
}

OneOf_FieldCalculationsPressureResultControlPressureType = Annotated[
    Union[TotalPressurePressureType, StaticPressurePressureType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIELD_CALCULATIONS_PRESSURE_RESULT_CONTROL_PRESSURE_TYPE_VARIANTS,
        )
    ),
]
