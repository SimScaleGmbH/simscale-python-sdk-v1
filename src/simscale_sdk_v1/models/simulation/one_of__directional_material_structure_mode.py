from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.allowed_direction import AllowedDirection
from simscale_sdk_v1.models.simulation.blocked_direction import BlockedDirection

# Choose the direction for applying fluid resistance:  Allowed: Fluid resistance is applied in the chosen direction, while fluid flow is blocked in the other two orthogonal directions. Blocked: Fluid flow is blocked in the chosen direction, and fluid resistance is applied in the other two orthogonal directions.
_ONE_OF__DIRECTIONAL_MATERIAL_STRUCTURE_MODE_VARIANTS: dict[str, type] = {
    "ALLOWED_DIRECTION": AllowedDirection,
    "BLOCKED_DIRECTION": BlockedDirection,
}

OneOf_DirectionalMaterialStructureMode = Annotated[
    Union[AllowedDirection, BlockedDirection],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIRECTIONAL_MATERIAL_STRUCTURE_MODE_VARIANTS,
        )
    ),
]
