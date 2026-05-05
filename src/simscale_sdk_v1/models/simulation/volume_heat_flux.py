from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__volumetric_power import DimensionalFunction_VolumetricPower
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class VolumeHeatFlux(SimScaleModel):
    """Specify the rate of heat transfer per unit volume within a body. Used for internal heat generation sources."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLUME_HEAT_FLUX",
        description="Specify the rate of heat transfer per unit volume within a body. Used for internal heat generation sources.  Schema name: VolumeHeatFlux",
    )
    name: str | None = Field(default=None)
    heat_flux_value: DimensionalFunction_VolumetricPower | None = Field(
        validation_alias="heatFluxValue", serialization_alias="heatFluxValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
