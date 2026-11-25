from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cartesian_component_vector_function import CartesianComponentVectorFunction
from simscale_sdk_v1.models.simulation.cylindrical_component_vector_function import CylindricalComponentVectorFunction

_ONE_OF__DIMENSIONAL_VECTOR_FUNCTION_WITH_LCS__TORQUE_VALUE_VARIANTS: dict[str, type] = {
    "CARTESIAN_COMPONENTS": CartesianComponentVectorFunction,
    "CYLINDRICAL_COMPONENTS": CylindricalComponentVectorFunction,
}

OneOf_DimensionalVectorFunctionWithLCS_TorqueValue = Annotated[
    Union[CartesianComponentVectorFunction, CylindricalComponentVectorFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIMENSIONAL_VECTOR_FUNCTION_WITH_LCS__TORQUE_VALUE_VARIANTS,
        )
    ),
]
