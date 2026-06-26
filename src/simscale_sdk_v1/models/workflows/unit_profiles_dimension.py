from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.unit_profile_dimension import UnitProfileDimension


class UnitProfilesDimension(SimScaleModel):
    """Holds unit profiles for a given quantity: one for the metric system, and an optional profile for the US customary system."""

    metric: UnitProfileDimension | None = Field(default=None)
    us_customary: UnitProfileDimension | None = Field(
        validation_alias="usCustomary", serialization_alias="usCustomary", default=None
    )
