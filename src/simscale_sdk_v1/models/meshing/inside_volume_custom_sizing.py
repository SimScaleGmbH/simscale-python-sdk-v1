from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__inside_volume_custom_sizing_sizing import (
    OneOf_InsideVolumeCustomSizingSizing,
)


class InsideVolumeCustomSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INSIDE_CUSTOM_SIZING",
        description="Schema name: InsideVolumeCustomSizing",
    )
    sizing: OneOf_InsideVolumeCustomSizingSizing | None = Field(default=None)
