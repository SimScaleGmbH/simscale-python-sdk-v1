from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_power import DimensionalFunction_VolumetricPower
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class TrSpecificPowerSource(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TR_SPECIFIC_POWER_SOURCE",
        description="Schema name: TrSpecificPowerSource",
    )
    name: str | None = Field(default=None)
    heat_flux: DimensionalFunction_VolumetricPower | None = Field(
        validation_alias="heatFlux", serialization_alias="heatFlux", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
