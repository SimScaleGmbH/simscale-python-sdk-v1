from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cartesian_component_partial_vector_function import (
    CartesianComponentPartialVectorFunction,
)
from simscale_sdk_v1.models.simulation.cylindrical_component_partial_vector_function import (
    CylindricalComponentPartialVectorFunction,
)

_ONE_OF__DIMENSIONAL_PARTIAL_VECTOR_FUNCTION_WITH_LCS__ANGLE_VALUE_VARIANTS: dict[str, type] = {
    "CARTESIAN_COMPONENTS": CartesianComponentPartialVectorFunction,
    "CYLINDRICAL_COMPONENTS": CylindricalComponentPartialVectorFunction,
}

OneOf_DimensionalPartialVectorFunctionWithLCS_AngleValue = Annotated[
    Union[CartesianComponentPartialVectorFunction, CylindricalComponentPartialVectorFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIMENSIONAL_PARTIAL_VECTOR_FUNCTION_WITH_LCS__ANGLE_VALUE_VARIANTS,
        )
    ),
]
