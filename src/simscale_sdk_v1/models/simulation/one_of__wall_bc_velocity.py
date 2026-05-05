from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.moving_wall_vbc import MovingWallVBC
from simscale_sdk_v1.models.simulation.no_slip_vbc import NoSlipVBC
from simscale_sdk_v1.models.simulation.rotating_wall_vbc import RotatingWallVBC
from simscale_sdk_v1.models.simulation.slip_vbc import SlipVBC

# Please choose the wall boundary condition sub-type based on the wall movement (U). Learn more.
_ONE_OF__WALL_BC_VELOCITY_VARIANTS: dict[str, type] = {
    "MOVING_WALL_VELOCITY": MovingWallVBC,
    "NO_SLIP": NoSlipVBC,
    "ROTATING_WALL_VELOCITY": RotatingWallVBC,
    "SLIP": SlipVBC,
}

OneOf_WallBCVelocity = Annotated[
    Union[MovingWallVBC, NoSlipVBC, RotatingWallVBC, SlipVBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WALL_BC_VELOCITY_VARIANTS,
        )
    ),
]
