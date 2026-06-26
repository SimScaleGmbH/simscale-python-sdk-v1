from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.measurement_unit_constant import MeasurementUnitConstant
from simscale_sdk_v1.models.workflows.measurement_unit_expression_select import MeasurementUnitExpressionSelect
from simscale_sdk_v1.models.workflows.measurement_unit_function_pow import MeasurementUnitFunctionPow
from simscale_sdk_v1.models.workflows.measurement_unit_operation_div import MeasurementUnitOperationDiv
from simscale_sdk_v1.models.workflows.measurement_unit_operation_times import MeasurementUnitOperationTimes
from simscale_sdk_v1.models.workflows.measurement_unit_reference import MeasurementUnitReference

# Value model for a measurement unit value. Resolves to a text JSON node.
_MEASUREMENT_UNIT_VALUE_VARIANTS: dict[str, type] = {
    "unit:constant": MeasurementUnitConstant,
    "unit:expression:select": MeasurementUnitExpressionSelect,
    "unit:function:pow": MeasurementUnitFunctionPow,
    "unit:operation:div": MeasurementUnitOperationDiv,
    "unit:operation:times": MeasurementUnitOperationTimes,
    "unit:reference": MeasurementUnitReference,
}

MeasurementUnitValue = Annotated[
    Union[
        MeasurementUnitConstant,
        MeasurementUnitExpressionSelect,
        MeasurementUnitFunctionPow,
        MeasurementUnitOperationDiv,
        MeasurementUnitOperationTimes,
        MeasurementUnitReference,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_MEASUREMENT_UNIT_VALUE_VARIANTS,
        )
    ),
]
