from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency
from simscale_sdk_v1.models.simulation.restricted_dimensional_function__frequency import (
    RestrictedDimensionalFunction_Frequency,
)


class FrequencyList(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LIST_V20",
        description="Schema name: FrequencyList",
    )
    start_frequency: Dimensional_Frequency | None = Field(
        validation_alias="startFrequency", serialization_alias="startFrequency", default=None
    )
    end_frequency: Dimensional_Frequency | None = Field(
        validation_alias="endFrequency", serialization_alias="endFrequency", default=None
    )
    frequency_stepping: RestrictedDimensionalFunction_Frequency | None = Field(
        validation_alias="frequencyStepping", serialization_alias="frequencyStepping", default=None
    )
