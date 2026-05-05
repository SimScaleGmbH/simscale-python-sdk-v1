from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency


class CoverSpectrum(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COVER_SPECTRUM",
        description="Schema name: CoverSpectrum",
    )
    start_frequency: Dimensional_Frequency | None = Field(
        validation_alias="startFrequency", serialization_alias="startFrequency", default=None
    )
    end_frequency: Dimensional_Frequency | None = Field(
        validation_alias="endFrequency", serialization_alias="endFrequency", default=None
    )
    frequencies_per_mode: int | None = Field(
        validation_alias="frequenciesPerMode",
        serialization_alias="frequenciesPerMode",
        default=10,
        description="Specify the number of excitation frequencies to be spread over each modal peak and neighbouring valleys. The eigenfrequency will also be considered when an even number is provided.",
    )
    growth_ratio: float | None = Field(
        validation_alias="growthRatio",
        serialization_alias="growthRatio",
        default=2.0,
        description="Ratio of the adjacent distances between excitation frequencies. It controls the distribution of the frequencies, with larger values resulting in a faster spread towards the valleys and tighter clustering around the modal peaks. Suggested value r >= 2.",
    )
