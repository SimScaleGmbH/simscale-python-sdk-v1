from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class HydrostaticFanPBC(SimScaleModel):
    """This pressure formulation is suitable for atmospheric flows with perfect gas fluids: the pressure decreases with increasing height to keep the domain at hydrostatic equilibrium. The ambient pressure in the input sets the pressure at ground level."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HYDROSTATIC_ISOTHERMAL_FAN_PRESSURE",
        description="This pressure formulation is suitable for atmospheric flows with perfect gas fluids: the pressure decreases with increasing height to keep the domain at hydrostatic equilibrium. The ambient pressure in the input sets the pressure at ground level.  Schema name: HydrostaticFanPBC",
    )
    fan_pressure: DimensionalFunction_Pressure | None = Field(
        validation_alias="fanPressure", serialization_alias="fanPressure", default=None
    )
    environmental_total_pressure: Dimensional_Pressure | None = Field(
        validation_alias="environmentalTotalPressure", serialization_alias="environmentalTotalPressure", default=None
    )
