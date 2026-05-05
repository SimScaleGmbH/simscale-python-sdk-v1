from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.constant_function import ConstantFunction
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class StrainHardeningModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN_HARDENING",
        description="Schema name: StrainHardeningModel",
    )
    yield_stress: DimensionalFunction_Pressure | None = Field(
        validation_alias="yieldStress", serialization_alias="yieldStress", default=None
    )
    ultimate_stress: DimensionalFunction_Pressure | None = Field(
        validation_alias="ultimateStress", serialization_alias="ultimateStress", default=None
    )
    ultimate_strain: ConstantFunction | None = Field(
        validation_alias="ultimateStrain", serialization_alias="ultimateStrain", default=None
    )
