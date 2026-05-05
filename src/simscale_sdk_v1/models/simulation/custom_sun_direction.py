from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class CustomSunDirection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_SOLAR_DIRECTION",
        description="Schema name: CustomSunDirection",
    )
    sun_direction_vector: DimensionalVector_Length | None = Field(
        validation_alias="sunDirectionVector", serialization_alias="sunDirectionVector", default=None
    )
