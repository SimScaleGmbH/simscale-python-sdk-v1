from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.dimensional_vector_constant import DimensionalVectorConstant
from simscale_sdk_v1.models.workflows.dimensional_vector_expression_select import DimensionalVectorExpressionSelect
from simscale_sdk_v1.models.workflows.dimensional_vector_from_components import DimensionalVectorFromComponents
from simscale_sdk_v1.models.workflows.dimensional_vector_function_norm import DimensionalVectorFunctionNorm
from simscale_sdk_v1.models.workflows.dimensional_vector_operation_div import DimensionalVectorOperationDiv
from simscale_sdk_v1.models.workflows.dimensional_vector_operation_minus import DimensionalVectorOperationMinus
from simscale_sdk_v1.models.workflows.dimensional_vector_operation_plus import DimensionalVectorOperationPlus
from simscale_sdk_v1.models.workflows.dimensional_vector_operation_times import DimensionalVectorOperationTimes
from simscale_sdk_v1.models.workflows.dimensional_vector_reference import DimensionalVectorReference

# Value model for a dimensional vector.  Resolves to an object node with field `vector` containing Cartesian vector components (`x`, `y`, `z`; as double nodes) and field `unit` (text node).  Note that during resolution, all dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s),
_DIMENSIONAL_VECTOR_VALUE_VARIANTS: dict[str, type] = {
    "dimensional_vector:constant": DimensionalVectorConstant,
    "dimensional_vector:expression:select": DimensionalVectorExpressionSelect,
    "dimensional_vector:function:norm": DimensionalVectorFunctionNorm,
    "dimensional_vector:operation:div": DimensionalVectorOperationDiv,
    "dimensional_vector:operation:minus": DimensionalVectorOperationMinus,
    "dimensional_vector:operation:plus": DimensionalVectorOperationPlus,
    "dimensional_vector:operation:times": DimensionalVectorOperationTimes,
    "dimensional_vector:reference": DimensionalVectorReference,
    "real:conversion:to_dimensional_vector": DimensionalVectorFromComponents,
}

DimensionalVectorValue = Annotated[
    Union[
        DimensionalVectorConstant,
        DimensionalVectorExpressionSelect,
        DimensionalVectorFunctionNorm,
        DimensionalVectorOperationDiv,
        DimensionalVectorOperationMinus,
        DimensionalVectorOperationPlus,
        DimensionalVectorOperationTimes,
        DimensionalVectorReference,
        DimensionalVectorFromComponents,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_DIMENSIONAL_VECTOR_VALUE_VARIANTS,
        )
    ),
]
