from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.marc_global_temperature_field_type import MarcGlobalTemperatureFieldType


class MarcTemperatureFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TEMPERATURE",
        description="Schema name: MarcTemperatureFieldSelection",
    )
    temperature_type: MarcGlobalTemperatureFieldType | None = Field(
        validation_alias="temperatureType", serialization_alias="temperatureType", default=None
    )
