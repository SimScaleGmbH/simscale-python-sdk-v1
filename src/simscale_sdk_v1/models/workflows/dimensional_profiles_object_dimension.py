from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.dimensional_profile_object_dimension import DimensionalProfileObjectDimension


class DimensionalProfilesObjectDimension(SimScaleModel):
    """Holds dimensional profiles for a given quantity: one for the metric system, and an optional profile for the US customary system."""

    metric: DimensionalProfileObjectDimension | None = Field(default=None)
    us_customary: DimensionalProfileObjectDimension | None = Field(
        validation_alias="usCustomary", serialization_alias="usCustomary", default=None
    )
