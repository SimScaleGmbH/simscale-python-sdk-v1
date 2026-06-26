from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.enum_constant import EnumConstant
from simscale_sdk_v1.models.workflows.enum_expression_select import EnumExpressionSelect
from simscale_sdk_v1.models.workflows.enum_reference import EnumReference

# Value model for an enum value. Resolves to a text JSON node.
_ENUM_VALUE_VARIANTS: dict[str, type] = {
    "enum:constant": EnumConstant,
    "enum:expression:select": EnumExpressionSelect,
    "enum:reference": EnumReference,
}

EnumValue = Annotated[
    Union[EnumConstant, EnumExpressionSelect, EnumReference],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_ENUM_VALUE_VARIANTS,
        )
    ),
]
