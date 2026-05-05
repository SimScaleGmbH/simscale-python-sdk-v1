from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fixed_value_pfbc import FixedValuePFBC
from simscale_sdk_v1.models.simulation.fixed_value_psbc import FixedValuePSBC
from simscale_sdk_v1.models.simulation.fixed_value_rhbc import FixedValueRHBC
from simscale_sdk_v1.models.simulation.hydrostatic_pressure import HydrostaticPressure
from simscale_sdk_v1.models.simulation.inlet_fixed_mf_values import InletFixedMFValues
from simscale_sdk_v1.models.simulation.inlet_fixed_pf_values import InletFixedPFValues
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_gauge_pressure import (
    OneOf_PressureInletBCGaugePressure,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_net_radiative_heat_flux import (
    OneOf_PressureInletBCNetRadiativeHeatFlux,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_pressure import OneOf_PressureInletBCPressure
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_pressure_rgh import OneOf_PressureInletBCPressureRgh
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_radiative_intensity_ray import (
    OneOf_PressureInletBCRadiativeIntensityRay,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_temperature import OneOf_PressureInletBCTemperature
from simscale_sdk_v1.models.simulation.one_of__pressure_inlet_bc_turbulence import OneOf_PressureInletBCTurbulence
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference
from simscale_sdk_v1.models.simulation.total_pbc import TotalPBC


class PressureInletBC(SimScaleModel):
    """This boundary condition is suitable for inlet and open boundaries where the value of pressure is known."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE_INLET_V31",
        description="This boundary condition is suitable for inlet and open boundaries where the value of pressure is known.  Schema name: PressureInletBC",
    )
    name: str | None = Field(default=None)
    pressure: OneOf_PressureInletBCPressure | None = Field(default=None)
    pressure_rgh: OneOf_PressureInletBCPressureRgh | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    gauge_pressure: OneOf_PressureInletBCGaugePressure | None = Field(
        validation_alias="gaugePressure", serialization_alias="gaugePressure", default=None
    )
    gauge_pressure_rgh: TotalPBC | None = Field(
        validation_alias="gaugePressureRgh", serialization_alias="gaugePressureRgh", default=None
    )
    turbulence: OneOf_PressureInletBCTurbulence | None = Field(default=None)
    temperature: OneOf_PressureInletBCTemperature | None = Field(default=None)
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
    hydrostatic_pressure: HydrostaticPressure | None = Field(
        validation_alias="hydrostaticPressure", serialization_alias="hydrostaticPressure", default=None
    )
    net_radiative_heat_flux: OneOf_PressureInletBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OneOf_PressureInletBCRadiativeIntensityRay | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    relative_humidity: FixedValueRHBC | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
