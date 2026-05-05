from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class ElectromagneticTransientControl(SimScaleModel):
    end_time: Dimensional_Time | None = Field(validation_alias="endTime", serialization_alias="endTime", default=None)
    time_increment: Dimensional_Time | None = Field(
        validation_alias="timeIncrement", serialization_alias="timeIncrement", default=None
    )
