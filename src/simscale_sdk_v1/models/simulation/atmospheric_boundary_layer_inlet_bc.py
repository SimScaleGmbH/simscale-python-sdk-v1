from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__speed import Dimensional_Speed
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class AtmosphericBoundaryLayerInletBC(SimScaleModel):
    """The atmospheric boundary layer boundary condition implements the standard logarithmic profile for the stream-wise wind velocity component with corresponding profiles for turbulence kinetic energy and specific dissipation rate, where the ground roughness effects are taken into account."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ATMOSPHERIC_BOUNDARY_LAYER_INLET",
        description="The atmospheric boundary layer boundary condition implements the standard logarithmic profile for the stream-wise wind velocity component with corresponding profiles for turbulence kinetic energy and specific dissipation rate, where the ground roughness effects are taken into account.  Schema name: AtmosphericBoundaryLayerInletBC",
    )
    name: str | None = Field(default=None)
    reference_velocity: Dimensional_Speed | None = Field(
        validation_alias="referenceVelocity", serialization_alias="referenceVelocity", default=None
    )
    reference_height: Dimensional_Length | None = Field(
        validation_alias="referenceHeight", serialization_alias="referenceHeight", default=None
    )
    ground_roughness: Dimensional_Length | None = Field(
        validation_alias="groundRoughness", serialization_alias="groundRoughness", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
