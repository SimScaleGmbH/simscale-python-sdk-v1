from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__power import DimensionalFunction_Power
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class TrAbsolutePowerSource(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TR_ABSOLUTE_POWER_SOURCE",
        description="Schema name: TrAbsolutePowerSource",
    )
    name: str | None = Field(default=None)
    heat_flux: DimensionalFunction_Power | None = Field(
        validation_alias="heatFlux", serialization_alias="heatFlux", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
