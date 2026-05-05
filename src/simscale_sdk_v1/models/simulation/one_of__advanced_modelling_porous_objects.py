from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.general_darcy_forchheimer_pacefish import GeneralDarcyForchheimerPacefish
from simscale_sdk_v1.models.simulation.porous_tree import PorousTree

_ONE_OF__ADVANCED_MODELLING_POROUS_OBJECTS_VARIANTS: dict[str, type] = {
    "GENERAL_POROSITY": GeneralDarcyForchheimerPacefish,
    "POROUS_TREE": PorousTree,
}

OneOf_AdvancedModellingPorousObjects = Annotated[
    Union[GeneralDarcyForchheimerPacefish, PorousTree],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_MODELLING_POROUS_OBJECTS_VARIANTS,
        )
    ),
]
