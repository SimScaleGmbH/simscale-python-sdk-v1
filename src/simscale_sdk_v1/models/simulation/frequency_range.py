from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency


class FrequencyRange(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="RANGE", description="Schema name: FrequencyRange"
    )
    start_frequency: Dimensional_Frequency | None = Field(
        validation_alias="startFrequency", serialization_alias="startFrequency", default=None
    )
    end_frequency: Dimensional_Frequency | None = Field(
        validation_alias="endFrequency", serialization_alias="endFrequency", default=None
    )
    number_of_sub_bands: int | None = Field(
        validation_alias="numberOfSubBands", serialization_alias="numberOfSubBands", default=1
    )
    parallelization_level: Literal["COMPLETE", "PARTIAL"] | None = Field(
        validation_alias="parallelizationLevel", serialization_alias="parallelizationLevel", default="COMPLETE"
    )
