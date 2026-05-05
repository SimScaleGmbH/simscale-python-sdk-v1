from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_net_radiative_heat_flux import (
    OneOf_VelocityOutletBCNetRadiativeHeatFlux,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_phase_fraction import (
    OneOf_VelocityOutletBCPhaseFraction,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_phase_fractions_v2 import (
    OneOf_VelocityOutletBCPhaseFractionsV2,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_radiative_intensity_ray import (
    OneOf_VelocityOutletBCRadiativeIntensityRay,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_outlet_bc_velocity import OneOf_VelocityOutletBCVelocity
from simscale_sdk_v1.models.simulation.outlet_back_flow_mf_values import OutletBackFlowMFValues
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class VelocityOutletBC(SimScaleModel):
    """This boundary condition imposes a known velocity-based constraint at an outlet."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VELOCITY_OUTLET_V7",
        description="This boundary condition imposes a known velocity-based constraint at an outlet.  Schema name: VelocityOutletBC",
    )
    name: str | None = Field(default=None)
    velocity: OneOf_VelocityOutletBCVelocity | None = Field(default=None)
    phase_fraction: OneOf_VelocityOutletBCPhaseFraction | None = Field(
        validation_alias="phaseFraction", serialization_alias="phaseFraction", default=None
    )
    phase_fractions_v2: OneOf_VelocityOutletBCPhaseFractionsV2 | None = Field(
        validation_alias="phaseFractionsV2", serialization_alias="phaseFractionsV2", default=None
    )
    mass_fractions_v2: OutletBackFlowMFValues | None = Field(
        validation_alias="massFractionsV2", serialization_alias="massFractionsV2", default=None
    )
    net_radiative_heat_flux: OneOf_VelocityOutletBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OneOf_VelocityOutletBCRadiativeIntensityRay | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
