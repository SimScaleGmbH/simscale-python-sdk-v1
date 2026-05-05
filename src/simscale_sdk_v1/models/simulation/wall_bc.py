from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__wall_bc_electric_boundary_condition import (
    OneOf_WallBCElectricBoundaryCondition,
)
from simscale_sdk_v1.models.simulation.one_of__wall_bc_net_radiative_heat_flux import OneOf_WallBCNetRadiativeHeatFlux
from simscale_sdk_v1.models.simulation.one_of__wall_bc_phase_fraction import OneOf_WallBCPhaseFraction
from simscale_sdk_v1.models.simulation.one_of__wall_bc_radiative_intensity_ray import OneOf_WallBCRadiativeIntensityRay
from simscale_sdk_v1.models.simulation.one_of__wall_bc_relative_humidity import OneOf_WallBCRelativeHumidity
from simscale_sdk_v1.models.simulation.one_of__wall_bc_temperature import OneOf_WallBCTemperature
from simscale_sdk_v1.models.simulation.one_of__wall_bc_velocity import OneOf_WallBCVelocity
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class WallBC(SimScaleModel):
    """This boundary provides several Solid Wall conditions.The default no-slip corresponds to friction wall with no movement. The slip wall models a surface with no friction. The rotating/moving wall model wall movement by prescribing velocities. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_V34",
        description="This boundary provides several Solid Wall conditions.The default no-slip corresponds to friction wall with no movement. The slip wall models a surface with no friction. The rotating/moving wall model wall movement by prescribing velocities. Learn more.  Schema name: WallBC",
    )
    name: str | None = Field(default=None)
    velocity: OneOf_WallBCVelocity | None = Field(default=None)
    temperature: OneOf_WallBCTemperature | None = Field(default=None)
    relative_humidity: OneOf_WallBCRelativeHumidity | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
    phase_fraction: OneOf_WallBCPhaseFraction | None = Field(
        validation_alias="phaseFraction", serialization_alias="phaseFraction", default=None
    )
    net_radiative_heat_flux: OneOf_WallBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OneOf_WallBCRadiativeIntensityRay | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    electric_boundary_condition: OneOf_WallBCElectricBoundaryCondition | None = Field(
        validation_alias="electricBoundaryCondition", serialization_alias="electricBoundaryCondition", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
