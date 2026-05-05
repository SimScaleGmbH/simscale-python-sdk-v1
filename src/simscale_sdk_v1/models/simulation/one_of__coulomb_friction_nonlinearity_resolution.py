from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_point_friction_non_linearity_resolution import (
    FixedPointFrictionNonLinearityResolution,
)
from simscale_sdk_v1.models.simulation.newton_friction_non_linearity_resolution import (
    NewtonFrictionNonLinearityResolution,
)

_ONE_OF__COULOMB_FRICTION_NONLINEARITY_RESOLUTION_VARIANTS: dict[str, type] = {
    "NEWTON_V29": NewtonFrictionNonLinearityResolution,
    "FIXED_POINT": FixedPointFrictionNonLinearityResolution,
}

OneOf_CoulombFrictionNonlinearityResolution = Annotated[
    Union[NewtonFrictionNonLinearityResolution, FixedPointFrictionNonLinearityResolution],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COULOMB_FRICTION_NONLINEARITY_RESOLUTION_VARIANTS,
        )
    ),
]
