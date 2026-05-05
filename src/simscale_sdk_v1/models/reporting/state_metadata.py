from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.automatic_state_metadata import AutomaticStateMetadata
from simscale_sdk_v1.models.reporting.default_state_metadata import DefaultStateMetadata
from simscale_sdk_v1.models.reporting.manual_state_metadata import ManualStateMetadata

_STATE_METADATA_VARIANTS: dict[str, type] = {
    "DEFAULT": DefaultStateMetadata,
    "AUTOMATIC": AutomaticStateMetadata,
    "MANUAL": ManualStateMetadata,
}

StateMetadata = Annotated[
    Union[DefaultStateMetadata, AutomaticStateMetadata, ManualStateMetadata],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="stateType",
            variants=_STATE_METADATA_VARIANTS,
        )
    ),
]
