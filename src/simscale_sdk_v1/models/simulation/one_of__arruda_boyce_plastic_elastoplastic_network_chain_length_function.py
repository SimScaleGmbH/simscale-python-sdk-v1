from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.constant_function import ConstantFunction
from simscale_sdk_v1.models.simulation.expression_function import ExpressionFunction
from simscale_sdk_v1.models.simulation.polynomial_function import PolynomialFunction
from simscale_sdk_v1.models.simulation.table_defined_function import TableDefinedFunction

# Defined by the number of statistically independent links (N) in a polymer chain, this determines the material's extensibility. It dictates the "locking stretch" point where chains become fully extended and the stress-strain curve turns sharply upward.
_ONE_OF__ARRUDA_BOYCE_PLASTIC_ELASTOPLASTIC_NETWORK_CHAIN_LENGTH_FUNCTION_VARIANTS: dict[str, type] = {
    "CONSTANT": ConstantFunction,
    "EXPRESSION": ExpressionFunction,
    "POLYNOMIAL": PolynomialFunction,
    "TABLE_DEFINED": TableDefinedFunction,
}

OneOf_ArrudaBoycePlasticElastoplasticNetworkChainLengthFunction = Annotated[
    Union[ConstantFunction, ExpressionFunction, PolynomialFunction, TableDefinedFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ARRUDA_BOYCE_PLASTIC_ELASTOPLASTIC_NETWORK_CHAIN_LENGTH_FUNCTION_VARIANTS,
        )
    ),
]
