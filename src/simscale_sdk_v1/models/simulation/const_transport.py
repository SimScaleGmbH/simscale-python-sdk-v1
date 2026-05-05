from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dynamic_viscosity import Dimensional_DynamicViscosity
from simscale_sdk_v1.models.simulation.dimensional_function__dynamic_viscosity import (
    DimensionalFunction_DynamicViscosity,
)
from simscale_sdk_v1.models.simulation.one_of__const_transport_thermo import OneOf_ConstTransportThermo


class ConstTransport(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="CONST", description="Schema name: ConstTransport"
    )
    dynamic_viscosity: Dimensional_DynamicViscosity | None = Field(
        validation_alias="dynamicViscosity", serialization_alias="dynamicViscosity", default=None
    )
    dynamic_viscosity_function: DimensionalFunction_DynamicViscosity | None = Field(
        validation_alias="dynamicViscosityFunction", serialization_alias="dynamicViscosityFunction", default=None
    )
    prandtl_number: float | None = Field(
        validation_alias="prandtlNumber",
        serialization_alias="prandtlNumber",
        default=None,
        description="Prandtl number (Pr) is the ratio of momentum transport to thermal tranport. Fluids with low Pr are free flowing and good for heat conduction.",
    )
    turbulent_prandtl_number: float | None = Field(
        validation_alias="turbulentPrandtlNumber",
        serialization_alias="turbulentPrandtlNumber",
        default=None,
        description="Turbulent Prandtl number is used to calculate the heat transfer due to turbulent effects in the domain.",
    )
    thermo: OneOf_ConstTransportThermo | None = Field(default=None)
