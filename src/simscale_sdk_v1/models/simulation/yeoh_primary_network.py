from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class YeohPrimaryNetwork(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="YEOH_PRIMARY_NETWORK",
        description="Schema name: YeohPrimaryNetwork",
    )
    c10: Dimensional_Pressure | None = Field(default=None)
    c20: Dimensional_Pressure | None = Field(default=None)
    c30: Dimensional_Pressure | None = Field(default=None)
    bulk_modulus: Dimensional_Pressure | None = Field(
        validation_alias="bulkModulus", serialization_alias="bulkModulus", default=None
    )
