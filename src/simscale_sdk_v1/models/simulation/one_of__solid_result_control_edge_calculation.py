from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.average_fields_calculation_result_control_item import (
    AverageFieldsCalculationResultControlItem,
)
from simscale_sdk_v1.models.simulation.min_max_fields_calculation_result_control_item import (
    MinMaxFieldsCalculationResultControlItem,
)
from simscale_sdk_v1.models.simulation.sum_fields_calculation_result_control_item import (
    SumFieldsCalculationResultControlItem,
)

_ONE_OF__SOLID_RESULT_CONTROL_EDGE_CALCULATION_VARIANTS: dict[str, type] = {
    "MIN_MAX_FIELDS_CALCULATION": MinMaxFieldsCalculationResultControlItem,
    "AVERAGE_FIELDS_CALCULATION": AverageFieldsCalculationResultControlItem,
    "SUM_FIELDS_CALCULATION": SumFieldsCalculationResultControlItem,
}

OneOf_SolidResultControlEdgeCalculation = Annotated[
    Union[
        MinMaxFieldsCalculationResultControlItem,
        AverageFieldsCalculationResultControlItem,
        SumFieldsCalculationResultControlItem,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_RESULT_CONTROL_EDGE_CALCULATION_VARIANTS,
        )
    ),
]
