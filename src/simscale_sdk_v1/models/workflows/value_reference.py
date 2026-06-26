from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.config_value_reference import ConfigValueReference
from simscale_sdk_v1.models.workflows.data_presence_reference import DataPresenceReference
from simscale_sdk_v1.models.workflows.data_value_reference import DataValueReference
from simscale_sdk_v1.models.workflows.general_metadata_value_reference import GeneralMetadataValueReference
from simscale_sdk_v1.models.workflows.iterator_reference import IteratorReference
from simscale_sdk_v1.models.workflows.metadata_value_reference import MetadataValueReference

# Reference to a value which can be resolved using a particular context.
_VALUE_REFERENCE_VARIANTS: dict[str, type] = {
    "config": ConfigValueReference,
    "data": DataValueReference,
    "data_presence": DataPresenceReference,
    "general_metadata": GeneralMetadataValueReference,
    "iterator": IteratorReference,
    "metadata": MetadataValueReference,
}

ValueReference = Annotated[
    Union[
        ConfigValueReference,
        DataValueReference,
        DataPresenceReference,
        GeneralMetadataValueReference,
        IteratorReference,
        MetadataValueReference,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_reference_type",
            variants=_VALUE_REFERENCE_VARIANTS,
        )
    ),
]
