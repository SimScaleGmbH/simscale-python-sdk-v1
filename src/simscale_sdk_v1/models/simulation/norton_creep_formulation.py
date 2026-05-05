from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__strain_rate import Dimensional_StrainRate


class NortonCreepFormulation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NORTON",
        description="Schema name: NortonCreepFormulation",
    )
    a: Dimensional_StrainRate | None = Field(default=None)
    n: float | None = Field(
        default=None, description="Define the parameter n of the Norton creep formulation: &epsilon;&#775; = A*&sigma;n"
    )
