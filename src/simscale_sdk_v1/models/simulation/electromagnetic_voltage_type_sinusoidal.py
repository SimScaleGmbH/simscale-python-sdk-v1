from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__electric_potential import Dimensional_ElectricPotential
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class ElectromagneticVoltageTypeSinusoidal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLTAGE_TYPE_SINUSOIDAL",
        description="Schema name: ElectromagneticVoltageTypeSinusoidal",
    )
    frequency: Dimensional_Frequency | None = Field(default=None)
    amplitude: Dimensional_ElectricPotential | None = Field(default=None)
    offset: Dimensional_ElectricPotential | None = Field(default=None)
    time_offset: Dimensional_Time | None = Field(
        validation_alias="timeOffset", serialization_alias="timeOffset", default=None
    )
