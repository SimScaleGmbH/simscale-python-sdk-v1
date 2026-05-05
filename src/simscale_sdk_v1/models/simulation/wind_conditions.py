from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.geographical_location import GeographicalLocation
from simscale_sdk_v1.models.simulation.wind_rose import WindRose


class WindConditions(SimScaleModel):
    geographical_location: GeographicalLocation | None = Field(
        validation_alias="geographicalLocation", serialization_alias="geographicalLocation", default=None
    )
    wind_rose: WindRose | None = Field(validation_alias="windRose", serialization_alias="windRose", default=None)
