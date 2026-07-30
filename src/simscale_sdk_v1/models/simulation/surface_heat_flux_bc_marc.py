from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__heat_flux import DimensionalFunction_HeatFlux
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SurfaceHeatFluxBCMarc(SimScaleModel):
    """Define the heatflux per unit area that enters the body through the assigned faces. Negative sign determines flux leaving the body."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_HEAT_FLUX",
        description="Define the heatflux per unit area that enters the body through the assigned faces. Negative sign determines flux leaving the body.  Schema name: SurfaceHeatFluxBCMarc",
    )
    name: str | None = Field(default=None)
    heatflux_value: DimensionalFunction_HeatFlux | None = Field(
        validation_alias="heatfluxValue", serialization_alias="heatfluxValue", default=None
    )
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
