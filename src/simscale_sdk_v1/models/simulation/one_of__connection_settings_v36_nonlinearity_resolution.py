from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_point_non_linearity_resolution import FixedPointNonLinearityResolution
from simscale_sdk_v1.models.simulation.newton_non_linearity_resolution import NewtonNonLinearityResolution

_ONE_OF__CONNECTION_SETTINGS_V36_NONLINEARITY_RESOLUTION_VARIANTS: dict[str, type] = {
    "NEWTON": NewtonNonLinearityResolution,
    "FIXED_POINT": FixedPointNonLinearityResolution,
}

OneOf_ConnectionSettingsV36NonlinearityResolution = Annotated[
    Union[NewtonNonLinearityResolution, FixedPointNonLinearityResolution],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONNECTION_SETTINGS_V36_NONLINEARITY_RESOLUTION_VARIANTS,
        )
    ),
]
