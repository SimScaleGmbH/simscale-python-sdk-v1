from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.boolean_field import BooleanField
from simscale_sdk_v1.models.workflows.integer_field import IntegerField
from simscale_sdk_v1.models.workflows.real_field import RealField
from simscale_sdk_v1.models.workflows.string_field import StringField

# Abstract base class for atomic fields.
_ATOMIC_FIELD_VARIANTS: dict[str, type] = {
    "BooleanField": BooleanField,
    "IntegerField": IntegerField,
    "RealField": RealField,
    "StringField": StringField,
}

AtomicField = Annotated[
    Union[BooleanField, IntegerField, RealField, StringField],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="schema_element_type",
            variants=_ATOMIC_FIELD_VARIANTS,
        )
    ),
]
