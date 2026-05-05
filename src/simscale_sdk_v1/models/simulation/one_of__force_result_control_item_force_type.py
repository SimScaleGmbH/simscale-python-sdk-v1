from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.global_nodal_force_type import GlobalNodalForceType
from simscale_sdk_v1.models.simulation.global_reaction_force_type import GlobalReactionForceType

_ONE_OF__FORCE_RESULT_CONTROL_ITEM_FORCE_TYPE_VARIANTS: dict[str, type] = {
    "REACTION": GlobalReactionForceType,
    "NODAL": GlobalNodalForceType,
}

OneOf_ForceResultControlItemForceType = Annotated[
    Union[GlobalReactionForceType, GlobalNodalForceType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FORCE_RESULT_CONTROL_ITEM_FORCE_TYPE_VARIANTS,
        )
    ),
]
