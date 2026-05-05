from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.nodal_force_type import NodalForceType
from simscale_sdk_v1.models.simulation.reaction_force_type import ReactionForceType

_ONE_OF__FORCE_FIELD_SELECTION_FORCE_TYPE_VARIANTS: dict[str, type] = {
    "REACTION": ReactionForceType,
    "NODAL": NodalForceType,
}

OneOf_ForceFieldSelectionForceType = Annotated[
    Union[ReactionForceType, NodalForceType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FORCE_FIELD_SELECTION_FORCE_TYPE_VARIANTS,
        )
    ),
]
