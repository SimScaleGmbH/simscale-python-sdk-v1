from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class YeohPrimaryNetwork(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="YEOH_PRIMARY_NETWORK",
        description="Schema name: YeohPrimaryNetwork",
    )
    c10_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="c10Function", serialization_alias="c10Function", default=None
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
