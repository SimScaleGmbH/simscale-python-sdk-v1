from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_transmittance import (
    DimensionalFunction_ThermalTransmittance,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ConvectiveHeatFlux(SimScaleModel):
    """Represents heat transfer between a surface and a fluid."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONVECTIVE_HEAT_FLUX",
        description="Represents heat transfer between a surface and a fluid.  Schema name: ConvectiveHeatFlux",
    )
    name: str | None = Field(default=None)
    heat_transfer_coefficient: DimensionalFunction_ThermalTransmittance | None = Field(
        validation_alias="heatTransferCoefficient", serialization_alias="heatTransferCoefficient", default=None
    )
    ambient_temperature: DimensionalFunction_Temperature | None = Field(
        validation_alias="ambientTemperature", serialization_alias="ambientTemperature", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
