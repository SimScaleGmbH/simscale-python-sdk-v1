from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.ambient_pbc import AmbientPBC
from simscale_sdk_v1.models.simulation.ambient_tbc import AmbientTBC
from simscale_sdk_v1.models.simulation.inlet_outlet_psbc import InletOutletPSBC
from simscale_sdk_v1.models.simulation.inlet_outlet_rhbc import InletOutletRHBC
from simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_net_radiative_heat_flux import (
    OneOf_NaturalConvectionInletOutletBCNetRadiativeHeatFlux,
)
from simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_pressure_rgh import (
    OneOf_NaturalConvectionInletOutletBCPressureRgh,
)
from simscale_sdk_v1.models.simulation.one_of__natural_convection_inlet_outlet_bc_turbulence import (
    OneOf_NaturalConvectionInletOutletBCTurbulence,
)
from simscale_sdk_v1.models.simulation.open_boundary_ray_bc import OpenBoundaryRayBC
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class NaturalConvectionInletOutletBC(SimScaleModel):
    """This boundary condition is suitable for an open boundary where the air can enter or exit freely from or to the atmosphere. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NATURAL_CONVECTION_INLET_OUTLET",
        description="This boundary condition is suitable for an open boundary where the air can enter or exit freely from or to the atmosphere. Learn more.  Schema name: NaturalConvectionInletOutletBC",
    )
    name: str | None = Field(default=None)
    pressure_rgh: OneOf_NaturalConvectionInletOutletBCPressureRgh | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    gauge_pressure_rgh: AmbientPBC | None = Field(
        validation_alias="gaugePressureRgh", serialization_alias="gaugePressureRgh", default=None
    )
    turbulence: OneOf_NaturalConvectionInletOutletBCTurbulence | None = Field(default=None)
    temperature: AmbientTBC | None = Field(default=None)
    passive_scalars: list[InletOutletPSBC] | None = Field(
        validation_alias="passiveScalars",
        serialization_alias="passiveScalars",
        default=None,
        description="Please choose a boundary condition for passive scalar (T).",
    )
    net_radiative_heat_flux: OneOf_NaturalConvectionInletOutletBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OpenBoundaryRayBC | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    relative_humidity: InletOutletRHBC | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
