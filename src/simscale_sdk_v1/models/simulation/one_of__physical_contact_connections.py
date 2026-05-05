from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.friction_contact import FrictionContact
from simscale_sdk_v1.models.simulation.frictionless_contact import FrictionlessContact

_ONE_OF__PHYSICAL_CONTACT_CONNECTIONS_VARIANTS: dict[str, type] = {
    "FRICTIONLESS_CONTACT": FrictionlessContact,
    "FRICTION_CONTACT": FrictionContact,
}

OneOf_PhysicalContactConnections = Annotated[
    Union[FrictionlessContact, FrictionContact],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PHYSICAL_CONTACT_CONNECTIONS_VARIANTS,
        )
    ),
]
