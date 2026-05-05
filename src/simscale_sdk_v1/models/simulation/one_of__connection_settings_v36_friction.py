from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.coulomb_friction import CoulombFriction
from simscale_sdk_v1.models.simulation.no_friction import NoFriction

_ONE_OF__CONNECTION_SETTINGS_V36_FRICTION_VARIANTS: dict[str, type] = {
    "NO_FRICTION": NoFriction,
    "COULOMB_FRICTION": CoulombFriction,
}

OneOf_ConnectionSettingsV36Friction = Annotated[
    Union[NoFriction, CoulombFriction],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONNECTION_SETTINGS_V36_FRICTION_VARIANTS,
        )
    ),
]
