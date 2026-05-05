from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__electric_current import Dimensional_ElectricCurrent
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class ElectromagneticCurrentTypeSinusoidal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CURRENT_TYPE_SINUSOIDAL",
        description="Schema name: ElectromagneticCurrentTypeSinusoidal",
    )
    frequency: Dimensional_Frequency | None = Field(default=None)
    amplitude: Dimensional_ElectricCurrent | None = Field(default=None)
    offset: Dimensional_ElectricCurrent | None = Field(default=None)
    time_offset: Dimensional_Time | None = Field(
        validation_alias="timeOffset", serialization_alias="timeOffset", default=None
    )
