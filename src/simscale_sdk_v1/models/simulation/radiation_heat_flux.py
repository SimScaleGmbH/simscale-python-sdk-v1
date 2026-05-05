from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RadiationHeatFlux(SimScaleModel):
    """Accounts for heat transfer due to thermal radiation between surfaces."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RADIATION_HEAT_FLUX",
        description="Accounts for heat transfer due to thermal radiation between surfaces.  Schema name: RadiationHeatFlux",
    )
    name: str | None = Field(default=None)
    emissivity: DimensionalFunction_Dimensionless | None = Field(default=None)
    ambient_temperature: DimensionalFunction_Temperature | None = Field(
        validation_alias="ambientTemperature", serialization_alias="ambientTemperature", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
