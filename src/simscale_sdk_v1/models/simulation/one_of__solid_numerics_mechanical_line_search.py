from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.false_line_search import FalseLineSearch
from simscale_sdk_v1.models.simulation.true_line_search import TrueLineSearch

_ONE_OF__SOLID_NUMERICS_MECHANICAL_LINE_SEARCH_VARIANTS: dict[str, type] = {
    "FALSE": FalseLineSearch,
    "TRUE": TrueLineSearch,
}

OneOf_SolidNumericsMechanicalLineSearch = Annotated[
    Union[FalseLineSearch, TrueLineSearch],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_NUMERICS_MECHANICAL_LINE_SEARCH_VARIANTS,
        )
    ),
]
