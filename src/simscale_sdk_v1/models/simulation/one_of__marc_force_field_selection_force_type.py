from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_external_force_type import MarcExternalForceType
from simscale_sdk_v1.models.simulation.marc_reaction_force_type import MarcReactionForceType

# Reaction force: The forces exerted by constraints (supports) to prevent motion; the sum of reaction forces typically balances the total external load.External force: The nodal representation of all applied loads, such as point loads and distributed loads, acting on the structure.
_ONE_OF__MARC_FORCE_FIELD_SELECTION_FORCE_TYPE_VARIANTS: dict[str, type] = {
    "REACTION": MarcReactionForceType,
    "EXTERNAL": MarcExternalForceType,
}

OneOf_MarcForceFieldSelectionForceType = Annotated[
    Union[MarcReactionForceType, MarcExternalForceType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_FORCE_FIELD_SELECTION_FORCE_TYPE_VARIANTS,
        )
    ),
]
