from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.isotropic_darcy_forchheimer import IsotropicDarcyForchheimer
from simscale_sdk_v1.models.simulation.rectifying_darcy_forchheimer import RectifyingDarcyForchheimer

_ONE_OF__DIRECTIONAL_DEPENDENCY_DARCY_FORCHHEIMER_TYPE_VARIANTS: dict[str, type] = {
    "ISOTROPIC": IsotropicDarcyForchheimer,
    "RECTIFYING": RectifyingDarcyForchheimer,
}

OneOf_DirectionalDependencyDarcyForchheimerType = Annotated[
    Union[IsotropicDarcyForchheimer, RectifyingDarcyForchheimer],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIRECTIONAL_DEPENDENCY_DARCY_FORCHHEIMER_TYPE_VARIANTS,
        )
    ),
]
