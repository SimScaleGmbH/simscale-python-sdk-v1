from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_point_contact_non_linearity_resolution import (
    FixedPointContactNonLinearityResolution,
)
from simscale_sdk_v1.models.simulation.newton_contact_non_linearity_resolution import (
    NewtonContactNonLinearityResolution,
)

_ONE_OF__CONNECTION_SETTINGS_V36_CONTACT_NON_LINEARITY_RESOLUTION_VARIANTS: dict[str, type] = {
    "NEWTON": NewtonContactNonLinearityResolution,
    "FIXED_POINT": FixedPointContactNonLinearityResolution,
}

OneOf_ConnectionSettingsV36ContactNonLinearityResolution = Annotated[
    Union[NewtonContactNonLinearityResolution, FixedPointContactNonLinearityResolution],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONNECTION_SETTINGS_V36_CONTACT_NON_LINEARITY_RESOLUTION_VARIANTS,
        )
    ),
]
