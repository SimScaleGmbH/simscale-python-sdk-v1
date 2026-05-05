from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class WallHeatTransferTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_HEAT_TRANSFER",
        description="Schema name: WallHeatTransferTBC",
    )
    wall_temperature: Dimensional_Temperature | None = Field(
        validation_alias="wallTemperature", serialization_alias="wallTemperature", default=None
    )
    thermal_diffusivity: Dimensional_KinematicViscosity | None = Field(
        validation_alias="thermalDiffusivity", serialization_alias="thermalDiffusivity", default=None
    )
