from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.imperfect_thermal_contact import ImperfectThermalContact
from simscale_sdk_v1.models.simulation.off_thermal_contact import OffThermalContact

_ONE_OF__MARC_BONDED_AND_TOUCHING_CONTACT_CONNECTION_THERMAL_CONTACT_VARIANTS: dict[str, type] = {
    "IMPERFECT": ImperfectThermalContact,
    "OFF": OffThermalContact,
}

OneOf_MarcBondedAndTouchingContactConnectionThermalContact = Annotated[
    Union[ImperfectThermalContact, OffThermalContact],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_BONDED_AND_TOUCHING_CONTACT_CONNECTION_THERMAL_CONTACT_VARIANTS,
        )
    ),
]
