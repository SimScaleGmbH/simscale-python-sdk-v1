from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.constant_contact_angle_pfbc import ConstantContactAnglePFBC
from simscale_sdk_v1.models.simulation.dynamic_contact_angle_pfbc import DynamicContactAnglePFBC
from simscale_sdk_v1.models.simulation.zero_gradient_pfbc import ZeroGradientPFBC

# Please choose a boundary condition for phase fraction (alpha).
_ONE_OF__WALL_BC_PHASE_FRACTION_VARIANTS: dict[str, type] = {
    "CONSTANT_CONTACT_ANGLE": ConstantContactAnglePFBC,
    "DYNAMIC_CONTACT_ANGLE": DynamicContactAnglePFBC,
    "ZERO_GRADIENT": ZeroGradientPFBC,
}

OneOf_WallBCPhaseFraction = Annotated[
    Union[ConstantContactAnglePFBC, DynamicContactAnglePFBC, ZeroGradientPFBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WALL_BC_PHASE_FRACTION_VARIANTS,
        )
    ),
]
