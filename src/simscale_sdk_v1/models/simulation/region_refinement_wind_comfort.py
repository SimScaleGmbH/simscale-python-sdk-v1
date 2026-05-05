from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__region_refinement_wind_comfort_new_fineness import (
    OneOf_RegionRefinementWindComfortNewFineness,
)


class RegionRefinementWindComfort(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REGION_REFINEMENT_WIND_COMFORT",
        description="Schema name: RegionRefinementWindComfort",
    )
    name: str | None = Field(default="Region refinement")
    new_fineness: OneOf_RegionRefinementWindComfortNewFineness | None = Field(
        validation_alias="newFineness", serialization_alias="newFineness", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
