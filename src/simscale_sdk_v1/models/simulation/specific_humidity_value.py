from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__mass_fraction import Dimensional_MassFraction


class SpecificHumidityValue(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIFIC_HUMIDITY_VALUE",
        description="Schema name: SpecificHumidityValue",
    )
    value: Dimensional_MassFraction | None = Field(default=None)
