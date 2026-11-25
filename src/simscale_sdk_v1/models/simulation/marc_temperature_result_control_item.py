from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.global_temperature import GlobalTemperature


class MarcTemperatureResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TEMPERATURE",
        description="Schema name: MarcTemperatureResultControlItem",
    )
    name: str | None = Field(default=None)
    temperature_type: GlobalTemperature | None = Field(
        validation_alias="temperatureType", serialization_alias="temperatureType", default=None
    )
