from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.dimensional_scalar_constant import DimensionalScalarConstant
from simscale_sdk_v1.models.workflows.dimensional_scalar_expression_select import DimensionalScalarExpressionSelect
from simscale_sdk_v1.models.workflows.dimensional_scalar_from_dimensional_vector_component import (
    DimensionalScalarFromDimensionalVectorComponent,
)
from simscale_sdk_v1.models.workflows.dimensional_scalar_function_pow import DimensionalScalarFunctionPow
from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_div import DimensionalScalarOperationDiv
from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_minus import DimensionalScalarOperationMinus
from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_plus import DimensionalScalarOperationPlus
from simscale_sdk_v1.models.workflows.dimensional_scalar_operation_times import DimensionalScalarOperationTimes
from simscale_sdk_v1.models.workflows.dimensional_scalar_reference import DimensionalScalarReference
from simscale_sdk_v1.models.workflows.dimensional_vector_function_mag import DimensionalVectorFunctionMag
from simscale_sdk_v1.models.workflows.integer_to_dimensional_scalar_value_conversion import (
    IntegerToDimensionalScalarValueConversion,
)
from simscale_sdk_v1.models.workflows.real_to_dimensional_scalar_value_conversion import (
    RealToDimensionalScalarValueConversion,
)

# Value model for a dimensional scalar.  Resolves to an object node with field `value` (double node) and field `unit` (text node).  Note: during resolution all dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s).
_DIMENSIONAL_SCALAR_VALUE_VARIANTS: dict[str, type] = {
    "dimensional_scalar:constant": DimensionalScalarConstant,
    "dimensional_scalar:expression:select": DimensionalScalarExpressionSelect,
    "dimensional_scalar:function:pow": DimensionalScalarFunctionPow,
    "dimensional_scalar:operation:div": DimensionalScalarOperationDiv,
    "dimensional_scalar:operation:minus": DimensionalScalarOperationMinus,
    "dimensional_scalar:operation:plus": DimensionalScalarOperationPlus,
    "dimensional_scalar:operation:times": DimensionalScalarOperationTimes,
    "dimensional_scalar:reference": DimensionalScalarReference,
    "dimensional_vector:function:component": DimensionalScalarFromDimensionalVectorComponent,
    "dimensional_vector:function:mag": DimensionalVectorFunctionMag,
    "integer:conversion:to_dimensional_scalar": IntegerToDimensionalScalarValueConversion,
    "real:conversion:to_dimensional_scalar": RealToDimensionalScalarValueConversion,
}

DimensionalScalarValue = Annotated[
    Union[
        DimensionalScalarConstant,
        DimensionalScalarExpressionSelect,
        DimensionalScalarFunctionPow,
        DimensionalScalarOperationDiv,
        DimensionalScalarOperationMinus,
        DimensionalScalarOperationPlus,
        DimensionalScalarOperationTimes,
        DimensionalScalarReference,
        DimensionalScalarFromDimensionalVectorComponent,
        DimensionalVectorFunctionMag,
        IntegerToDimensionalScalarValueConversion,
        RealToDimensionalScalarValueConversion,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_DIMENSIONAL_SCALAR_VALUE_VARIANTS,
        )
    ),
]
