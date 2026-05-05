from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.pressure_coefficient_result_type import PressureCoefficientResultType
from simscale_sdk_v1.models.simulation.pressure_value_result_type import PressureValueResultType

_ONE_OF__FIELD_CALCULATIONS_PRESSURE_RESULT_CONTROL_RESULT_TYPE_VARIANTS: dict[str, type] = {
    "PRESSURE_VALUE": PressureValueResultType,
    "PRESSURE_COEFFICIENT": PressureCoefficientResultType,
}

OneOf_FieldCalculationsPressureResultControlResultType = Annotated[
    Union[PressureValueResultType, PressureCoefficientResultType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIELD_CALCULATIONS_PRESSURE_RESULT_CONTROL_RESULT_TYPE_VARIANTS,
        )
    ),
]
