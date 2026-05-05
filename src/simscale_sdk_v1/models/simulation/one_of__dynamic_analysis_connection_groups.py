from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.contact import Contact
from simscale_sdk_v1.models.simulation.physical_contact import PhysicalContact

_ONE_OF__DYNAMIC_ANALYSIS_CONNECTION_GROUPS_VARIANTS: dict[str, type] = {
    "CONTACT": Contact,
    "PHYSICAL_CONTACT_V36": PhysicalContact,
}

OneOf_DynamicAnalysisConnectionGroups = Annotated[
    Union[Contact, PhysicalContact],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DYNAMIC_ANALYSIS_CONNECTION_GROUPS_VARIANTS,
        )
    ),
]
