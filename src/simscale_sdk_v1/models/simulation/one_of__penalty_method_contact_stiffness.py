from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.custom_contact_stiffness import CustomContactStiffness
from simscale_sdk_v1.models.simulation.high_contact_stiffness import HighContactStiffness
from simscale_sdk_v1.models.simulation.low_contact_stiffness import LowContactStiffness
from simscale_sdk_v1.models.simulation.moderate_contact_stiffness import ModerateContactStiffness

# Define the stiffness for the contact pair. A higher stiffness reduces interpenetration but may also lead to numerical instabilities and divergence. The independence of the results from this parameter should be checked.
_ONE_OF__PENALTY_METHOD_CONTACT_STIFFNESS_VARIANTS: dict[str, type] = {
    "LOW_CONTACT_STIFFNESS": LowContactStiffness,
    "MODERATE_CONTACT_STIFFNESS": ModerateContactStiffness,
    "HIGH_CONTACT_STIFFNESS": HighContactStiffness,
    "CUSTOM_CONTACT_STIFFNESS": CustomContactStiffness,
}

OneOf_PenaltyMethodContactStiffness = Annotated[
    Union[LowContactStiffness, ModerateContactStiffness, HighContactStiffness, CustomContactStiffness],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PENALTY_METHOD_CONTACT_STIFFNESS_VARIANTS,
        )
    ),
]
