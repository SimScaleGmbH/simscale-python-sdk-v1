from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__mass_flow_rate import Dimensional_MassFlowRate
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SpeciesHumiditySource(SimScaleModel):
    """Humidity sources can be used to simulate humidity generation from a volume, knowing the mass of species entering the fluid domain per second."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIES_MASS_FLOW_RATE",
        description="Humidity sources can be used to simulate humidity generation from a volume, knowing the mass of species entering the fluid domain per second.  Schema name: SpeciesHumiditySource",
    )
    name: str | None = Field(default=None)
    water_vapor_mass_rate: Dimensional_MassFlowRate | None = Field(
        validation_alias="waterVaporMassRate", serialization_alias="waterVaporMassRate", default=None
    )
    dry_air_mass_rate: Dimensional_MassFlowRate | None = Field(
        validation_alias="dryAirMassRate", serialization_alias="dryAirMassRate", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
