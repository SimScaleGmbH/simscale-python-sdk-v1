from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.parametric.numerical_sequence_parameter_value_generator import (
    NumericalSequenceParameterValueGenerator,
)


class ParameterWithValueGenerator(SimScaleModel):
    value_source: str = Field(
        validation_alias="valueSource",
        serialization_alias="valueSource",
        default="GENERATOR",
        description="Schema name: ParameterWithValueGenerator",
    )
    name: str | None = Field(default=None)
    path: str | None = Field(default=None)
    value_generator: NumericalSequenceParameterValueGenerator | None = Field(
        validation_alias="valueGenerator", serialization_alias="valueGenerator", default=None
    )
