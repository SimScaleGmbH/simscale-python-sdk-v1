from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bonded_contact import BondedContact
from simscale_sdk_v1.models.simulation.sliding_contact import SlidingContact

_ONE_OF__CONTACT_CONNECTIONS_VARIANTS: dict[str, type] = {
    "BONDED_CONTACT": BondedContact,
    "SLIDING_CONTACT": SlidingContact,
}

OneOf_ContactConnections = Annotated[
    Union[BondedContact, SlidingContact],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONTACT_CONNECTIONS_VARIANTS,
        )
    ),
]
