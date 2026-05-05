from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__inlet_outlet_rhbc_humidity_value import (
    OneOf_InletOutletRHBCHumidityValue,
)


class InletOutletRHBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_OUTLET",
        description="Schema name: InletOutletRHBC",
    )
    humidity_value: OneOf_InletOutletRHBCHumidityValue | None = Field(
        validation_alias="humidityValue", serialization_alias="humidityValue", default=None
    )
