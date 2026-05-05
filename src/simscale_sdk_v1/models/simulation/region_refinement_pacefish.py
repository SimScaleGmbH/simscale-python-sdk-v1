from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class RegionRefinementPacefish(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_PACEFISH",
        description="Schema name: RegionRefinementPacefish",
    )
    name: str | None = Field(default="Region refinement")
    target_resolution: Dimensional_Length | None = Field(
        validation_alias="targetResolution", serialization_alias="targetResolution", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
