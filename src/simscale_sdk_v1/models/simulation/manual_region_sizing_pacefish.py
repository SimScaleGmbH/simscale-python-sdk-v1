from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class ManualRegionSizingPacefish(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_REGION_PACEFISH",
        description="Schema name: ManualRegionSizingPacefish",
    )
    target_resolution: Dimensional_Length | None = Field(
        validation_alias="targetResolution", serialization_alias="targetResolution", default=None
    )
