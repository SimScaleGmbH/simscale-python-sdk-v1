from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.reynolds_stress_result_type import ReynoldsStressResultType
from simscale_sdk_v1.models.simulation.y_plus_ras_result_type import YPlusRASResultType

_ONE_OF__FIELD_CALCULATIONS_TURBULENCE_RESULT_CONTROL_RESULT_TYPE_VARIANTS: dict[str, type] = {
    "DIMENSIONLESS_WALL_DISTANCE_YPLUS": YPlusRASResultType,
    "REYNOLDS_STRESS_TENSOR": ReynoldsStressResultType,
}

OneOf_FieldCalculationsTurbulenceResultControlResultType = Annotated[
    Union[YPlusRASResultType, ReynoldsStressResultType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIELD_CALCULATIONS_TURBULENCE_RESULT_CONTROL_RESULT_TYPE_VARIANTS,
        )
    ),
]
