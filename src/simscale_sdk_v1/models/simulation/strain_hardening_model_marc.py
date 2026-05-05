from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class StrainHardeningModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN_HARDENING",
        description="Schema name: StrainHardeningModelMarc",
    )
    ultimate_tensile_stress: Dimensional_Pressure | None = Field(
        validation_alias="ultimateTensileStress", serialization_alias="ultimateTensileStress", default=None
    )
    ultimate_total_strain: Dimensional_Dimensionless | None = Field(
        validation_alias="ultimateTotalStrain", serialization_alias="ultimateTotalStrain", default=None
    )
