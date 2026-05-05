from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.ambient_tbc import AmbientTBC
from simscale_sdk_v1.models.simulation.hydrostatic_pressure import HydrostaticPressure
from simscale_sdk_v1.models.simulation.inlet_outlet_rhbc import InletOutletRHBC
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_gauge_pressure import (
    OneOf_PressureOutletBCGaugePressure,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_gauge_pressure_rgh import (
    OneOf_PressureOutletBCGaugePressureRgh,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_net_radiative_heat_flux import (
    OneOf_PressureOutletBCNetRadiativeHeatFlux,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_phase_fractions_v2 import (
    OneOf_PressureOutletBCPhaseFractionsV2,
)
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_pressure import OneOf_PressureOutletBCPressure
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_pressure_rgh import OneOf_PressureOutletBCPressureRgh
from simscale_sdk_v1.models.simulation.one_of__pressure_outlet_bc_radiative_intensity_ray import (
    OneOf_PressureOutletBCRadiativeIntensityRay,
)
from simscale_sdk_v1.models.simulation.outlet_back_flow_mf_values import OutletBackFlowMFValues
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PressureOutletBC(SimScaleModel):
    """This boundary condition allows to specify a pressure value at an outlet boundary."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE_OUTLET_V30",
        description="This boundary condition allows to specify a pressure value at an outlet boundary.  Schema name: PressureOutletBC",
    )
    name: str | None = Field(default=None)
    pressure: OneOf_PressureOutletBCPressure | None = Field(default=None)
    pressure_rgh: OneOf_PressureOutletBCPressureRgh | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    gauge_pressure: OneOf_PressureOutletBCGaugePressure | None = Field(
        validation_alias="gaugePressure", serialization_alias="gaugePressure", default=None
    )
    phase_fractions_v2: OneOf_PressureOutletBCPhaseFractionsV2 | None = Field(
        validation_alias="phaseFractionsV2", serialization_alias="phaseFractionsV2", default=None
    )
    mass_fractions_v2: OutletBackFlowMFValues | None = Field(
        validation_alias="massFractionsV2", serialization_alias="massFractionsV2", default=None
    )
    hydrostatic_pressure: HydrostaticPressure | None = Field(
        validation_alias="hydrostaticPressure", serialization_alias="hydrostaticPressure", default=None
    )
    gauge_pressure_rgh: OneOf_PressureOutletBCGaugePressureRgh | None = Field(
        validation_alias="gaugePressureRgh", serialization_alias="gaugePressureRgh", default=None
    )
    net_radiative_heat_flux: OneOf_PressureOutletBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OneOf_PressureOutletBCRadiativeIntensityRay | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    relative_humidity: InletOutletRHBC | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
    temperature: AmbientTBC | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
