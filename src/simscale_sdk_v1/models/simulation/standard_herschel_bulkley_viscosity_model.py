from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional__dynamic_viscosity import Dimensional_DynamicViscosity
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional__strain_rate import Dimensional_StrainRate


class StandardHerschelBulkleyViscosityModel(SimScaleModel):
    """Choose between Newtonian and Non-Newtonian viscosity models."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STD_HERSCHEL_BULKLEY",
        description="Choose between Newtonian and Non-Newtonian viscosity models.  Schema name: StandardHerschelBulkleyViscosityModel",
    )
    consistency: Dimensional_DynamicViscosity | None = Field(default=None)
    flow_index: Dimensional_Dimensionless | None = Field(
        validation_alias="flowIndex", serialization_alias="flowIndex", default=None
    )
    fluid_yield_stress: Dimensional_Pressure | None = Field(
        validation_alias="fluidYieldStress", serialization_alias="fluidYieldStress", default=None
    )
    critical_shear_rate: Dimensional_StrainRate | None = Field(
        validation_alias="criticalShearRate", serialization_alias="criticalShearRate", default=None
    )
