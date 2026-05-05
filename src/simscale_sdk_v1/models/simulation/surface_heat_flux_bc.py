from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__heat_flux import DimensionalFunction_HeatFlux
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SurfaceHeatFluxBC(SimScaleModel):
    """Define the heatflux per unit area that enters the body through the assigned faces. Negative sign determines flux leaving the body."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_HEAT_FLUX",
        description="Define the heatflux per unit area that enters the body through the assigned faces. Negative sign determines flux leaving the body.  Schema name: SurfaceHeatFluxBC",
    )
    name: str | None = Field(default=None)
    heatflux_value: DimensionalFunction_HeatFlux | None = Field(
        validation_alias="heatfluxValue", serialization_alias="heatfluxValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
