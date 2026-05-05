from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.newton_krylov_resolution_type import NewtonKrylovResolutionType
from simscale_sdk_v1.models.simulation.newton_resolution_type import NewtonResolutionType

_ONE_OF__SOLID_NUMERICS_MECHANICAL_RESOLUTION_TYPE_VARIANTS: dict[str, type] = {
    "NEWTON": NewtonResolutionType,
    "NEWTON_KRYLOV": NewtonKrylovResolutionType,
}

OneOf_SolidNumericsMechanicalResolutionType = Annotated[
    Union[NewtonResolutionType, NewtonKrylovResolutionType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_NUMERICS_MECHANICAL_RESOLUTION_TYPE_VARIANTS,
        )
    ),
]
