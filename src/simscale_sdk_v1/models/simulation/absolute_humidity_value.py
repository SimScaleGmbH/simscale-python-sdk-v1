from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density


class AbsoluteHumidityValue(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE_HUMIDITY_VALUE",
        description="Schema name: AbsoluteHumidityValue",
    )
    value: Dimensional_Density | None = Field(default=None)
