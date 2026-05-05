from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.constant_function import ConstantFunction
from simscale_sdk_v1.models.simulation.expression_function import ExpressionFunction
from simscale_sdk_v1.models.simulation.polynomial_function import PolynomialFunction
from simscale_sdk_v1.models.simulation.table_defined_function import TableDefinedFunction

_ONE_OF__DIMENSIONAL_FUNCTION__POWER_VALUE_VARIANTS: dict[str, type] = {
    "CONSTANT": ConstantFunction,
    "EXPRESSION": ExpressionFunction,
    "POLYNOMIAL": PolynomialFunction,
    "TABLE_DEFINED": TableDefinedFunction,
}

OneOf_DimensionalFunction_PowerValue = Annotated[
    Union[ConstantFunction, ExpressionFunction, PolynomialFunction, TableDefinedFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIMENSIONAL_FUNCTION__POWER_VALUE_VARIANTS,
        )
    ),
]
