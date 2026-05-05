from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.h_const_thermo import HConstThermo
from simscale_sdk_v1.models.simulation.standard_herschel_bulkley_viscosity_model import (
    StandardHerschelBulkleyViscosityModel,
)


class HerschelBulkleyTransport(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HERSCHEL_BULKLEY",
        description="Schema name: HerschelBulkleyTransport",
    )
    viscosity_model: StandardHerschelBulkleyViscosityModel | None = Field(
        validation_alias="viscosityModel", serialization_alias="viscosityModel", default=None
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
    thermo: HConstThermo | None = Field(default=None)
