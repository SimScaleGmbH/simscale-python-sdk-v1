from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.distance_volume_custom_sizing import DistanceVolumeCustomSizing
from simscale_sdk_v1.models.meshing.inside_volume_custom_sizing import InsideVolumeCustomSizing

_ONE_OF__VOLUME_CUSTOM_SIZING_CUSTOM_SIZING_MODES_VARIANTS: dict[str, type] = {
    "DISTANCE_CUSTOM_SIZING": DistanceVolumeCustomSizing,
    "INSIDE_CUSTOM_SIZING": InsideVolumeCustomSizing,
}

OneOf_VolumeCustomSizingCustomSizingModes = Annotated[
    Union[DistanceVolumeCustomSizing, InsideVolumeCustomSizing],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VOLUME_CUSTOM_SIZING_CUSTOM_SIZING_MODES_VARIANTS,
        )
    ),
]
