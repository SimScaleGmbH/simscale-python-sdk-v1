from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.false_semi_implicit import FalseSemiImplicit
from simscale_sdk_v1.models.simulation.true_semi_implicit import TrueSemiImplicit

_ONE_OF_MULES_SOLVER_SEMI_IMPLICIT_VARIANTS: dict[str, type] = {
    "FALSE_SEMI_IMPLICIT": FalseSemiImplicit,
    "TRUE_SEMI_IMPLICIT": TrueSemiImplicit,
}

OneOf_MULESSolverSemiImplicit = Annotated[
    Union[FalseSemiImplicit, TrueSemiImplicit],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_MULES_SOLVER_SEMI_IMPLICIT_VARIANTS,
        )
    ),
]
