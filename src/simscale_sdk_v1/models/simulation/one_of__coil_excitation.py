from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.current_excitation import CurrentExcitation
from simscale_sdk_v1.models.simulation.voltage_excitation import VoltageExcitation

# Current ExcitationUse when you want to set a specific current flow through the coil. Note that the specified current is assumed to flow over the sum of all entry (or internal) faces.Voltage ExcitationUse when you want to set a specific voltage across the coil ports.
_ONE_OF__COIL_EXCITATION_VARIANTS: dict[str, type] = {
    "CURRENT_EXCITATION": CurrentExcitation,
    "VOLTAGE_EXCITATION": VoltageExcitation,
}

OneOf_CoilExcitation = Annotated[
    Union[CurrentExcitation, VoltageExcitation],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__COIL_EXCITATION_VARIANTS,
        )
    ),
]
