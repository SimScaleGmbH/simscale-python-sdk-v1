from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FractionValueInitialCondition(SimScaleModel):
    fraction_value: float | None = Field(
        validation_alias="fractionValue", serialization_alias="fractionValue", default=0.0
    )
