from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_power import DimensionalFunction_VolumetricPower
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SpecificPowerSource(SimScaleModel):
    """Power sources can be used to simulate heat generation from a volume. Three types are available:Absolute: Used when total power emitted by the assigned volume is known.Specific: Used when power density of the assigned volume is known.Heat exchanger: Used to model a heat exchanger on a fluid region. The heat input is computed from the total conductance (U [W/K]) and the difference between the fluid temperature (T) and the heat exchanger temperature (Tref). Q = U (T - Tref). Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIFIC_V23",
        description="Power sources can be used to simulate heat generation from a volume. Three types are available:Absolute: Used when total power emitted by the assigned volume is known.Specific: Used when power density of the assigned volume is known.Heat exchanger: Used to model a heat exchanger on a fluid region. The heat input is computed from the total conductance (U [W/K]) and the difference between the fluid temperature (T) and the heat exchanger temperature (Tref). Q = U (T - Tref). Learn more.  Schema name: SpecificPowerSource",
    )
    name: str | None = Field(default=None)
    heat_flux: DimensionalFunction_VolumetricPower | None = Field(
        validation_alias="heatFlux", serialization_alias="heatFlux", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
