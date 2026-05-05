from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.wind_rose_velocity_bucket import WindRoseVelocityBucket


class WindRose(SimScaleModel):
    num_directions: int | None = Field(
        validation_alias="numDirections", serialization_alias="numDirections", default=16
    )
    velocity_buckets: list[WindRoseVelocityBucket] | None = Field(
        validation_alias="velocityBuckets", serialization_alias="velocityBuckets", default=None
    )
    velocity_unit: str = Field(validation_alias="velocityUnit", serialization_alias="velocityUnit", default="m/s")
    exposure_categories: list[Literal["EC1", "EC2", "EC3", "EC4", "EC5", "EC6"]] | None = Field(
        validation_alias="exposureCategories", serialization_alias="exposureCategories", default=None
    )
    wind_engineering_standard: Literal["EU", "AS_NZS", "NEN8100", "LONDON", "AIJ"] | None = Field(
        validation_alias="windEngineeringStandard", serialization_alias="windEngineeringStandard", default="EU"
    )
    wind_data_source: Literal["METEOBLUE", "USER_UPLOAD"] | None = Field(
        validation_alias="windDataSource", serialization_alias="windDataSource", default=None
    )
    add_surface_roughness: bool | None = Field(
        validation_alias="addSurfaceRoughness", serialization_alias="addSurfaceRoughness", default=True
    )
    gust_factor_v2: float | None = Field(
        validation_alias="gustFactorV2", serialization_alias="gustFactorV2", default=2.5
    )
