from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NumericalSequenceParameterValueGenerator(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NUMERICAL_SEQUENCE",
        description="Schema name: NumericalSequenceParameterValueGenerator",
    )
    start: float | None = Field(default=None)
    end: float | None = Field(default=None)
    step: float | None = Field(default=None)
    inclusive: bool
