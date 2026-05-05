from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fixed_value_pfbc import FixedValuePFBC
from simscale_sdk_v1.models.simulation.fixed_value_psbc import FixedValuePSBC
from simscale_sdk_v1.models.simulation.fixed_value_rhbc import FixedValueRHBC
from simscale_sdk_v1.models.simulation.inlet_fixed_mf_values import InletFixedMFValues
from simscale_sdk_v1.models.simulation.inlet_fixed_pf_values import InletFixedPFValues
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_dissipation_type import (
    OneOf_VelocityInletBCDissipationType,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_net_radiative_heat_flux import (
    OneOf_VelocityInletBCNetRadiativeHeatFlux,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_radiative_intensity_ray import (
    OneOf_VelocityInletBCRadiativeIntensityRay,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_temperature import OneOf_VelocityInletBCTemperature
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_turbulence import OneOf_VelocityInletBCTurbulence
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_turbulence_intensity import (
    OneOf_VelocityInletBCTurbulenceIntensity,
)
from simscale_sdk_v1.models.simulation.one_of__velocity_inlet_bc_velocity import OneOf_VelocityInletBCVelocity
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class VelocityInletBC(SimScaleModel):
    """This boundary condition imposes a known velocity-based constraint at an inlet."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VELOCITY_INLET_V3",
        description="This boundary condition imposes a known velocity-based constraint at an inlet.  Schema name: VelocityInletBC",
    )
    name: str | None = Field(default=None)
    velocity: OneOf_VelocityInletBCVelocity | None = Field(default=None)
    turbulence: OneOf_VelocityInletBCTurbulence | None = Field(default=None)
    temperature: OneOf_VelocityInletBCTemperature | None = Field(default=None)
    passive_scalars: list[FixedValuePSBC] | None = Field(
        validation_alias="passiveScalars",
        serialization_alias="passiveScalars",
        default=None,
        description="Please choose a boundary condition for passive scalar (T).",
    )
    phase_fraction: FixedValuePFBC | None = Field(
        validation_alias="phaseFraction", serialization_alias="phaseFraction", default=None
    )
    phase_fractions_v2: InletFixedPFValues | None = Field(
        validation_alias="phaseFractionsV2", serialization_alias="phaseFractionsV2", default=None
    )
    mass_fractions_v2: InletFixedMFValues | None = Field(
        validation_alias="massFractionsV2", serialization_alias="massFractionsV2", default=None
    )
    turbulence_intensity: OneOf_VelocityInletBCTurbulenceIntensity | None = Field(
        validation_alias="turbulenceIntensity", serialization_alias="turbulenceIntensity", default=None
    )
    dissipation_type: OneOf_VelocityInletBCDissipationType | None = Field(
        validation_alias="dissipationType", serialization_alias="dissipationType", default=None
    )
    net_radiative_heat_flux: OneOf_VelocityInletBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OneOf_VelocityInletBCRadiativeIntensityRay | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    relative_humidity: FixedValueRHBC | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
