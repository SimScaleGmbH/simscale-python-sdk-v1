from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class DistanceSizing(SimScaleModel):
    distance: Dimensional_Length | None = Field(default=None)
    default_size: Dimensional_Length | None = Field(
        validation_alias="defaultSize", serialization_alias="defaultSize", default=None
    )
    min_size: Dimensional_Length | None = Field(validation_alias="minSize", serialization_alias="minSize", default=None)
