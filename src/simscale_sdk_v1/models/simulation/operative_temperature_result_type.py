from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OperativeTemperatureResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OPERATIVE_TEMPERATURE",
        description="Schema name: OperativeTemperatureResultType",
    )
