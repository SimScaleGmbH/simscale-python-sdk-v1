from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class StrainHardeningModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN_HARDENING",
        description="Schema name: StrainHardeningModelMarc",
    )
    ultimate_tensile_stress_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="ultimateTensileStressFunction",
        serialization_alias="ultimateTensileStressFunction",
        default=None,
    )
    ultimate_total_strain_function: DimensionalFunction_Dimensionless | None = Field(
        validation_alias="ultimateTotalStrainFunction", serialization_alias="ultimateTotalStrainFunction", default=None
    )
