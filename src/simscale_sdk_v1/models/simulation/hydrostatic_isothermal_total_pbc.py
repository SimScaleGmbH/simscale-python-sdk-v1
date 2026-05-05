from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class HydrostaticIsothermalTotalPBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HYDROSTATIC_ISOTHERMAL_TOTAL_PRESSURE",
        description="Schema name: HydrostaticIsothermalTotalPBC",
    )
    ambient_pressure: Dimensional_Pressure | None = Field(
        validation_alias="ambientPressure", serialization_alias="ambientPressure", default=None
    )
