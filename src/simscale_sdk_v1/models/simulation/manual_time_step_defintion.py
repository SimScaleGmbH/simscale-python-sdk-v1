from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.dimensional_function__time import DimensionalFunction_Time


class ManualTimeStepDefintion(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL",
        description="Schema name: ManualTimeStepDefintion",
    )
    end_time: Dimensional_Time | None = Field(validation_alias="endTime", serialization_alias="endTime", default=None)
    time_step_length: DimensionalFunction_Time | None = Field(
        validation_alias="timeStepLength", serialization_alias="timeStepLength", default=None
    )
    cutbacks: int | None = Field(
        default=10,
        description="The maximum number of times to cut down the time step in each increment when convergence criteria are not met.",
    )
