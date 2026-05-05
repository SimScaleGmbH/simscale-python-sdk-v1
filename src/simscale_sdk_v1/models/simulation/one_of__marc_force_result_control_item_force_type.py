from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.external_force import ExternalForce
from simscale_sdk_v1.models.simulation.reaction_force import ReactionForce

# Reaction force: The forces exerted by constraints (supports) to prevent motion; the sum of reaction forces typically balances the total external load.External force: The nodal representation of all applied loads, such as point loads and distributed loads, acting on the structure.
_ONE_OF__MARC_FORCE_RESULT_CONTROL_ITEM_FORCE_TYPE_VARIANTS: dict[str, type] = {
    "REACTION": ReactionForce,
    "EXTERNAL": ExternalForce,
}

OneOf_MarcForceResultControlItemForceType = Annotated[
    Union[ReactionForce, ExternalForce],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_FORCE_RESULT_CONTROL_ITEM_FORCE_TYPE_VARIANTS,
        )
    ),
]
