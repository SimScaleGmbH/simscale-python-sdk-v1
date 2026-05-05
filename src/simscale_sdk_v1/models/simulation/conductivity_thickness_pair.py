from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__electric_resistivity import Dimensional_ElectricResistivity
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__thermal_conductivity import Dimensional_ThermalConductivity


class ConductivityThicknessPair(SimScaleModel):
    thermal_conductivity: Dimensional_ThermalConductivity | None = Field(
        validation_alias="thermalConductivity", serialization_alias="thermalConductivity", default=None
    )
    electric_resistivity: Dimensional_ElectricResistivity | None = Field(
        validation_alias="electricResistivity", serialization_alias="electricResistivity", default=None
    )
    layer_thickness: Dimensional_Length | None = Field(
        validation_alias="layerThickness", serialization_alias="layerThickness", default=None
    )
