from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class TwoTerms(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="TWO_TERMS", description="Schema name: TwoTerms"
    )
    modulus1: Dimensional_Pressure | None = Field(default=None)
    exponent1: float | None = Field(default=0.0)
    modulus2: Dimensional_Pressure | None = Field(default=None)
    exponent2: float | None = Field(default=0.0)
