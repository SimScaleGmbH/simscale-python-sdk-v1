from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency


class CenterFrequency(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CENTER",
        description="Schema name: CenterFrequency",
    )
    center_frequency: Dimensional_Frequency | None = Field(
        validation_alias="centerFrequency", serialization_alias="centerFrequency", default=None
    )
    number_of_modes: int | None = Field(
        validation_alias="numberOfModes",
        serialization_alias="numberOfModes",
        default=10,
        description="Define the maximum number of eigenfrequencies/eigenmodes, that should be calculated.",
    )
