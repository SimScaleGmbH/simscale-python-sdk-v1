from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.marc_bonded_and_touching_contact_connection import (
    MarcBondedAndTouchingContactConnection,
)
from simscale_sdk_v1.models.simulation.marc_bonded_contact_connection import MarcBondedContactConnection
from simscale_sdk_v1.models.simulation.marc_touching_contact_connection import MarcTouchingContactConnection

_ONE_OF__MARC_CONNECTION_GROUP_CONNECTIONS_VARIANTS: dict[str, type] = {
    "BONDED": MarcBondedContactConnection,
    "TOUCHING": MarcTouchingContactConnection,
    "BONDED_AND_TOUCHING": MarcBondedAndTouchingContactConnection,
}

OneOf_MarcConnectionGroupConnections = Annotated[
    Union[MarcBondedContactConnection, MarcTouchingContactConnection, MarcBondedAndTouchingContactConnection],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_CONNECTION_GROUP_CONNECTIONS_VARIANTS,
        )
    ),
]
