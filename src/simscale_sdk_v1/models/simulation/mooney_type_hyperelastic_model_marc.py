from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class MooneyTypeHyperelasticModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MOONEY_TYPE_MARC",
        description="Schema name: MooneyTypeHyperelasticModelMarc",
    )
    c10: Dimensional_Pressure | None = Field(default=None)
    c01: Dimensional_Pressure | None = Field(default=None)
    c11: Dimensional_Pressure | None = Field(default=None)
    c20: Dimensional_Pressure | None = Field(default=None)
    c30: Dimensional_Pressure | None = Field(default=None)
    bulk_modulus: Dimensional_Pressure | None = Field(
        validation_alias="bulkModulus", serialization_alias="bulkModulus", default=None
    )
