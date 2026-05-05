from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency


class SingleFrequency(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SINGLE",
        description="Schema name: SingleFrequency",
    )
    frequency: Dimensional_Frequency | None = Field(default=None)
