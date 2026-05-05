from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__heat_flux import DimensionalFunction_HeatFlux
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SurfaceHeatFlux(SimScaleModel):
    """Specify the rate of heat transfer per unit area at the boundary. Used for heating or cooling surfaces."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_HEAT_FLUX",
        description="Specify the rate of heat transfer per unit area at the boundary. Used for heating or cooling surfaces.  Schema name: SurfaceHeatFlux",
    )
    name: str | None = Field(default=None)
    heat_flux_value: DimensionalFunction_HeatFlux | None = Field(
        validation_alias="heatFluxValue", serialization_alias="heatFluxValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
