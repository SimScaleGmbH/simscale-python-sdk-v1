from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless


class PronySeries(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRONY_SERIES",
        description="Schema name: PronySeries",
    )
    prony_factors: DimensionalFunction_Dimensionless | None = Field(
        validation_alias="pronyFactors", serialization_alias="pronyFactors", default=None
    )
