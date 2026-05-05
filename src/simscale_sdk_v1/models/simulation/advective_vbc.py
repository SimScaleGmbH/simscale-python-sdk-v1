from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed


class AdvectiveVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ADVECTIVE",
        description="Schema name: AdvectiveVBC",
    )
    relax_boundary: bool | None = Field(
        validation_alias="relaxBoundary", serialization_alias="relaxBoundary", default=False
    )
    far_field_value: DimensionalVector_Speed | None = Field(
        validation_alias="farFieldValue", serialization_alias="farFieldValue", default=None
    )
    relaxation_length_scale: Dimensional_Length | None = Field(
        validation_alias="relaxationLengthScale", serialization_alias="relaxationLengthScale", default=None
    )
