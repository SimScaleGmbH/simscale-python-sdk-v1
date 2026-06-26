from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.constant_value_list import ConstantValueList
from simscale_sdk_v1.models.workflows.integer_sequence_generator import IntegerSequenceGenerator
from simscale_sdk_v1.models.workflows.real_sequence_generator import RealSequenceGenerator
from simscale_sdk_v1.models.workflows.reference_value_list import ReferenceValueList
from simscale_sdk_v1.models.workflows.value_list_expression_select import ValueListExpressionSelect
from simscale_sdk_v1.models.workflows.value_list_function_drop import ValueListFunctionDrop
from simscale_sdk_v1.models.workflows.value_list_function_drop_last import ValueListFunctionDropLast
from simscale_sdk_v1.models.workflows.value_list_function_filter import ValueListFunctionFilter
from simscale_sdk_v1.models.workflows.value_list_function_map import ValueListFunctionMap
from simscale_sdk_v1.models.workflows.value_list_function_sub_list import ValueListFunctionSubList
from simscale_sdk_v1.models.workflows.value_list_function_take import ValueListFunctionTake
from simscale_sdk_v1.models.workflows.value_list_function_take_last import ValueListFunctionTakeLast
from simscale_sdk_v1.models.workflows.value_list_operation_plus import ValueListOperationPlus
from simscale_sdk_v1.models.workflows.value_list_operation_times import ValueListOperationTimes

# Value model for a list of values. Resolves to a JSON array.
_VALUE_LIST_STRING_VALUE_VARIANTS: dict[str, type] = {
    "list:constant": ConstantValueList,
    "list:expression:select": ValueListExpressionSelect,
    "list:function:drop": ValueListFunctionDrop,
    "list:function:drop_last": ValueListFunctionDropLast,
    "list:function:filter": ValueListFunctionFilter,
    "list:function:map": ValueListFunctionMap,
    "list:function:sublist": ValueListFunctionSubList,
    "list:function:take": ValueListFunctionTake,
    "list:function:take_last": ValueListFunctionTakeLast,
    "list:generator:integer_sequence": IntegerSequenceGenerator,
    "list:generator:real_sequence": RealSequenceGenerator,
    "list:operation:plus": ValueListOperationPlus,
    "list:operation:times": ValueListOperationTimes,
    "list:reference": ReferenceValueList,
}

ValueListStringValue = Annotated[
    Union[
        ConstantValueList,
        ValueListExpressionSelect,
        ValueListFunctionDrop,
        ValueListFunctionDropLast,
        ValueListFunctionFilter,
        ValueListFunctionMap,
        ValueListFunctionSubList,
        ValueListFunctionTake,
        ValueListFunctionTakeLast,
        IntegerSequenceGenerator,
        RealSequenceGenerator,
        ValueListOperationPlus,
        ValueListOperationTimes,
        ReferenceValueList,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_VALUE_LIST_STRING_VALUE_VARIANTS,
        )
    ),
]
