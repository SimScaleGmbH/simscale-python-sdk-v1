from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_average_fields_calculation_result_control_item import (
    MarcAverageFieldsCalculationResultControlItem,
)
from simscale_sdk_v1.models.simulation.marc_min_max_fields_calculation_result_control_item import (
    MarcMinMaxFieldsCalculationResultControlItem,
)
from simscale_sdk_v1.models.simulation.marc_sum_fields_calculation_result_control_item import (
    MarcSumFieldsCalculationResultControlItem,
)

_ONE_OF__MARC_RESULT_CONTROL_AREA_CALCULATION_VARIANTS: dict[str, type] = {
    "MIN_MAX_FIELDS_CALCULATION": MarcMinMaxFieldsCalculationResultControlItem,
    "AVERAGE_FIELDS_CALCULATION": MarcAverageFieldsCalculationResultControlItem,
    "SUM_FIELDS_CALCULATION": MarcSumFieldsCalculationResultControlItem,
}

OneOf_MarcResultControlAreaCalculation = Annotated[
    Union[
        MarcMinMaxFieldsCalculationResultControlItem,
        MarcAverageFieldsCalculationResultControlItem,
        MarcSumFieldsCalculationResultControlItem,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_RESULT_CONTROL_AREA_CALCULATION_VARIANTS,
        )
    ),
]
