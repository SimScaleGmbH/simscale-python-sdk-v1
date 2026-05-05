from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.component_vector_function import ComponentVectorFunction
from simscale_sdk_v1.models.simulation.table_defined_vector_function import TableDefinedVectorFunction

_ONE_OF__DIMENSIONAL_VECTOR_FUNCTION__SPEED_VALUE_VARIANTS: dict[str, type] = {
    "COMPONENT": ComponentVectorFunction,
    "TABLE_DEFINED": TableDefinedVectorFunction,
}

OneOf_DimensionalVectorFunction_SpeedValue = Annotated[
    Union[ComponentVectorFunction, TableDefinedVectorFunction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIMENSIONAL_VECTOR_FUNCTION__SPEED_VALUE_VARIANTS,
        )
    ),
]
