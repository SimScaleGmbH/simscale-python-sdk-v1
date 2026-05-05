from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__strain_rate import Dimensional_StrainRate


class TimeHardeningCreepFormulation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TIME_HARDENING",
        description="Schema name: TimeHardeningCreepFormulation",
    )
    a: Dimensional_StrainRate | None = Field(default=None)
    n: float | None = Field(
        default=None,
        description="Define the parameter n of the Time Hardening creep formulation: &epsilon;&#775; = A*&sigma;n*tm",
    )
    m: float | None = Field(
        default=None,
        description="Define the parameter m of the Time Hardening creep formulation: &epsilon;&#775; = A*&sigma;n*tm",
    )
