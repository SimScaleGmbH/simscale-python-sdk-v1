from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TemperatureResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TEMPERATURE",
        description="Schema name: TemperatureResultControlItem",
    )
    name: str | None = Field(default=None)
    temperature_type: Literal["FIELD"] | None = Field(
        validation_alias="temperatureType", serialization_alias="temperatureType", default="FIELD"
    )
