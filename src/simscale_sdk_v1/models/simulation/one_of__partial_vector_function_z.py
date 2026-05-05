from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.prescribed_optional_function import PrescribedOptionalFunction
from simscale_sdk_v1.models.simulation.unconstrained_optional_function import UnconstrainedOptionalFunction

_ONE_OF__PARTIAL_VECTOR_FUNCTION_Z_VARIANTS: dict[str, type] = {
    "PRESCRIBED": PrescribedOptionalFunction,
    "UNCONSTRAINED": UnconstrainedOptionalFunction,
}

OneOf_PartialVectorFunctionZ = Annotated[
    Union[PrescribedOptionalFunction, UnconstrainedOptionalFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PARTIAL_VECTOR_FUNCTION_Z_VARIANTS,
        )
    ),
]
