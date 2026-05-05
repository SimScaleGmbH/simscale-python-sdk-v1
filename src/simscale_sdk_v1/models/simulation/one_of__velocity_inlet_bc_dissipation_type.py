from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_omega_dissipation import AutomaticOmegaDissipation
from simscale_sdk_v1.models.simulation.custom_omega_dissipation import CustomOmegaDissipation

_ONE_OF__VELOCITY_INLET_BC_DISSIPATION_TYPE_VARIANTS: dict[str, type] = {
    "AUTOMATIC_DISSIPATION": AutomaticOmegaDissipation,
    "CUSTOM_DISSIPATION": CustomOmegaDissipation,
}

OneOf_VelocityInletBCDissipationType = Annotated[
    Union[AutomaticOmegaDissipation, CustomOmegaDissipation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_INLET_BC_DISSIPATION_TYPE_VARIANTS,
        )
    ),
]
