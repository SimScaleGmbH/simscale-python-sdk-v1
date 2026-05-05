from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional__thermal_transmittance import Dimensional_ThermalTransmittance


class WallConvectionModel(SimScaleModel):
    convection_coefficient: Dimensional_ThermalTransmittance | None = Field(
        validation_alias="convectionCoefficient", serialization_alias="convectionCoefficient", default=None
    )
    ambient_temperature: Dimensional_Temperature | None = Field(
        validation_alias="ambientTemperature", serialization_alias="ambientTemperature", default=None
    )
