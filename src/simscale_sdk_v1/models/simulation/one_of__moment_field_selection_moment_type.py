from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.nodal_moment_type import NodalMomentType
from simscale_sdk_v1.models.simulation.reaction_moment_type import ReactionMomentType

_ONE_OF__MOMENT_FIELD_SELECTION_MOMENT_TYPE_VARIANTS: dict[str, type] = {
    "REACTION": ReactionMomentType,
    "NODAL": NodalMomentType,
}

OneOf_MomentFieldSelectionMomentType = Annotated[
    Union[ReactionMomentType, NodalMomentType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MOMENT_FIELD_SELECTION_MOMENT_TYPE_VARIANTS,
        )
    ),
]
