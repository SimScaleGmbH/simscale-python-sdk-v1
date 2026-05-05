from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.contact_gap_type import ContactGapType
from simscale_sdk_v1.models.simulation.contact_normal_force_type import ContactNormalForceType
from simscale_sdk_v1.models.simulation.contact_pressure_type import ContactPressureType
from simscale_sdk_v1.models.simulation.contact_state_type import ContactStateType

_ONE_OF__CONTACT_FIELD_SELECTION_CONTACT_TYPE_VARIANTS: dict[str, type] = {
    "PRESSURE": ContactPressureType,
    "NORMAL_FORCE": ContactNormalForceType,
    "GAP": ContactGapType,
    "STATE": ContactStateType,
}

OneOf_ContactFieldSelectionContactType = Annotated[
    Union[ContactPressureType, ContactNormalForceType, ContactGapType, ContactStateType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONTACT_FIELD_SELECTION_CONTACT_TYPE_VARIANTS,
        )
    ),
]
