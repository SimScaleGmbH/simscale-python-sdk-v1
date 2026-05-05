from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.geographical_location import GeographicalLocation


class TimeAndPlaceSunDirection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TIME_AND_PLACE",
        description="Schema name: TimeAndPlaceSunDirection",
    )
    north_angle: Dimensional_Angle | None = Field(
        validation_alias="northAngle", serialization_alias="northAngle", default=None
    )
    geographical_location: GeographicalLocation | None = Field(
        validation_alias="geographicalLocation", serialization_alias="geographicalLocation", default=None
    )
    local_date_time: str | None = Field(
        validation_alias="localDateTime", serialization_alias="localDateTime", default=None
    )
