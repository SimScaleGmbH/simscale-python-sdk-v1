from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__fixed_value_rhbc_humidity_value import OneOf_FixedValueRHBCHumidityValue


class FixedValueRHBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE",
        description="Schema name: FixedValueRHBC",
    )
    humidity_value: OneOf_FixedValueRHBCHumidityValue | None = Field(
        validation_alias="humidityValue", serialization_alias="humidityValue", default=None
    )
