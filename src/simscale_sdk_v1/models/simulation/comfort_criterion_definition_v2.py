from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__speed import DimensionalFunction_Speed


class ComfortCriterionDefinitionV2(SimScaleModel):
    wind_speed_thresholds: DimensionalFunction_Speed | None = Field(
        validation_alias="windSpeedThresholds", serialization_alias="windSpeedThresholds", default=None
    )
