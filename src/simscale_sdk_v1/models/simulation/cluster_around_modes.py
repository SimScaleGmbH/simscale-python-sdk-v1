from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency


class ClusterAroundModes(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CLUSTER_AROUND_MODES",
        description="Schema name: ClusterAroundModes",
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
        default=5,
        description="Specify the number of excitation frequencies to be clustered around each eigenfrequency. The eigenfrequency itself will also be considered when an even number is provided.",
    )
    percentage_spread: float | None = Field(
        validation_alias="percentageSpread",
        serialization_alias="percentageSpread",
        default=10.0,
        description="Define the total bandwidth around each eigenfrequency, as a percentage of each individual eigenfrequency, within which excitation frequencies will be spaced. If a value of 10% is given, the bandwidth will extend 5% of the eigenfrequency value on both sides of the eigenfrequency.",
    )
