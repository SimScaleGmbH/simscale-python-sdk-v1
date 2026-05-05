from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.constant_function import ConstantFunction
from simscale_sdk_v1.models.simulation.expression_function import ExpressionFunction
from simscale_sdk_v1.models.simulation.polynomial_function import PolynomialFunction
from simscale_sdk_v1.models.simulation.table_defined_function import TableDefinedFunction

# Provide the Poisson's ratio value which describes the compression or elongation of a material transverse to axial strain. Poisson's ratio can have a value within range from -1 to 0.5. Important remarks: Value less than 0 means that material is auxetic.Most of the metals such as steel and aluminum have value between 0.2 to 0.35 and are considered compressible.Value of 0.5 means that the material is incompressible such as rubber and some types of foams. Please avoid giving this value since it leads to convergence problem. You can give 0.499 rather than 0.5.
_ONE_OF__ELASTICITY_MARC_POISSONS_RATIO_VARIANTS: dict[str, type] = {
    "CONSTANT": ConstantFunction,
    "EXPRESSION": ExpressionFunction,
    "POLYNOMIAL": PolynomialFunction,
    "TABLE_DEFINED": TableDefinedFunction,
}

OneOf_ElasticityMarcPoissonsRatio = Annotated[
    Union[ConstantFunction, ExpressionFunction, PolynomialFunction, TableDefinedFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELASTICITY_MARC_POISSONS_RATIO_VARIANTS,
        )
    ),
]
