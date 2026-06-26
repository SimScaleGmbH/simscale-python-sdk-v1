from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.data_repository.external_data_info import ExternalDataInfo
from simscale_sdk_v1.models.data_repository.internal_data_info import InternalDataInfo

# Information about one data entity. General metadata about the associated piece of business data.
_DATA_INFO_VARIANTS: dict[str, type] = {
    "externalDataInfo": ExternalDataInfo,
    "internalDataInfo": InternalDataInfo,
}

DataInfo = Annotated[
    Union[ExternalDataInfo, InternalDataInfo],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="data_info_type",
            variants=_DATA_INFO_VARIANTS,
        )
    ),
]
