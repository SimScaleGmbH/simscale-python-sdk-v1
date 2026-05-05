from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class HydrostaticIsothermalPBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HYDROSTATIC_ISOTHERMAL_PRESSURE",
        description="Schema name: HydrostaticIsothermalPBC",
    )
    ambient_static_pressure: Dimensional_Pressure | None = Field(
        validation_alias="ambientStaticPressure", serialization_alias="ambientStaticPressure", default=None
    )
