from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class MooneyTypeHyperelasticModelMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MOONEY_TYPE_MARC",
        description="Schema name: MooneyTypeHyperelasticModelMarc",
    )
    c10_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="c10Function", serialization_alias="c10Function", default=None
    )
    c01_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="c01Function", serialization_alias="c01Function", default=None
    )
    c11_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="c11Function", serialization_alias="c11Function", default=None
    )
    c20_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="c20Function", serialization_alias="c20Function", default=None
    )
    c30_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="c30Function", serialization_alias="c30Function", default=None
    )
    bulk_modulus_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="bulkModulusFunction", serialization_alias="bulkModulusFunction", default=None
    )
