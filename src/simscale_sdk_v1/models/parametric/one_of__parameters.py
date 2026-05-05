from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.parametric.parameter_with_value_generator import ParameterWithValueGenerator
from simscale_sdk_v1.models.parametric.parameter_with_values import ParameterWithValues

_ONE_OF__PARAMETERS_VARIANTS: dict[str, type] = {
    "CONFIGURATION": ParameterWithValues,
    "GENERATOR": ParameterWithValueGenerator,
}

OneOf_Parameters = Annotated[
    Union[ParameterWithValues, ParameterWithValueGenerator],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="valueSource",
            variants=_ONE_OF__PARAMETERS_VARIANTS,
        )
    ),
]
