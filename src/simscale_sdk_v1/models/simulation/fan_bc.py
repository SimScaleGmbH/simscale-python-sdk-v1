from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fan_pbc import FanPBC
from simscale_sdk_v1.models.simulation.fixed_value_psbc import FixedValuePSBC
from simscale_sdk_v1.models.simulation.fixed_value_rhbc import FixedValueRHBC
from simscale_sdk_v1.models.simulation.one_of__fan_bc_net_radiative_heat_flux import OneOf_FanBCNetRadiativeHeatFlux
from simscale_sdk_v1.models.simulation.one_of__fan_bc_pressure_rgh import OneOf_FanBCPressureRgh
from simscale_sdk_v1.models.simulation.one_of__fan_bc_radiative_intensity_ray import OneOf_FanBCRadiativeIntensityRay
from simscale_sdk_v1.models.simulation.one_of__fan_bc_temperature import OneOf_FanBCTemperature
from simscale_sdk_v1.models.simulation.one_of__fan_bc_turbulence import OneOf_FanBCTurbulence
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FanBC(SimScaleModel):
    """This boundary condition sets the pressure based on the pressure drop specified as a function of the volumetric flow rate. Learn more"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FAN",
        description="This boundary condition sets the pressure based on the pressure drop specified as a function of the volumetric flow rate. Learn more  Schema name: FanBC",
    )
    name: str | None = Field(default=None)
    direction: Literal["IN", "OUT"] | None = Field(default="IN")
    pressure: FanPBC | None = Field(default=None)
    pressure_rgh: OneOf_FanBCPressureRgh | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    gauge_pressure: FanPBC | None = Field(
        validation_alias="gaugePressure", serialization_alias="gaugePressure", default=None
    )
    gauge_pressure_rgh: FanPBC | None = Field(
        validation_alias="gaugePressureRgh", serialization_alias="gaugePressureRgh", default=None
    )
    turbulence: OneOf_FanBCTurbulence | None = Field(default=None)
    temperature: OneOf_FanBCTemperature | None = Field(default=None)
    passive_scalars: list[FixedValuePSBC] | None = Field(
        validation_alias="passiveScalars",
        serialization_alias="passiveScalars",
        default=None,
        description="Please choose a boundary condition for passive scalar (T).",
    )
    net_radiative_heat_flux: OneOf_FanBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    radiative_intensity_ray: OneOf_FanBCRadiativeIntensityRay | None = Field(
        validation_alias="radiativeIntensityRay", serialization_alias="radiativeIntensityRay", default=None
    )
    relative_humidity: FixedValueRHBC | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
