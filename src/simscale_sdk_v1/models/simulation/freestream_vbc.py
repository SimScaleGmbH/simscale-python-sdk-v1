from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed
from simscale_sdk_v1.models.simulation.one_of__freestream_vbc_ambient_pressure import OneOf_FreestreamVBCAmbientPressure


class FreestreamVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FREESTREAM",
        description="Schema name: FreestreamVBC",
    )
    value: DimensionalVector_Speed | None = Field(default=None)
    ambient_pressure: OneOf_FreestreamVBCAmbientPressure | None = Field(
        validation_alias="ambientPressure", serialization_alias="ambientPressure", default=None
    )
