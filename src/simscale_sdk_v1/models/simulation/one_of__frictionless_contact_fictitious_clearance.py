from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.no_fictitious_clearance import NoFictitiousClearance
from simscale_sdk_v1.models.simulation.with_fictitious_clearance import WithFictitiousClearance

_ONE_OF__FRICTIONLESS_CONTACT_FICTITIOUS_CLEARANCE_VARIANTS: dict[str, type] = {
    "NO_FICTITIOUS_CLEARANCE": NoFictitiousClearance,
    "WITH_FICTITIOUS_CLEARANCE": WithFictitiousClearance,
}

OneOf_FrictionlessContactFictitiousClearance = Annotated[
    Union[NoFictitiousClearance, WithFictitiousClearance],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FRICTIONLESS_CONTACT_FICTITIOUS_CLEARANCE_VARIANTS,
        )
    ),
]
