from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class PerfectPlasticityModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PERFECT_PLASTICITY",
        description="Schema name: PerfectPlasticityModel",
    )
    yield_stress: DimensionalFunction_Pressure | None = Field(
        validation_alias="yieldStress", serialization_alias="yieldStress", default=None
    )
