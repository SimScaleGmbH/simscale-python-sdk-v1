from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.parametric.any_of__parameter_with_values_values import AnyOf_ParameterWithValuesValues


class ParameterWithValues(SimScaleModel):
    value_source: str = Field(
        validation_alias="valueSource",
        serialization_alias="valueSource",
        default="CONFIGURATION",
        description="Schema name: ParameterWithValues",
    )
    name: str | None = Field(default=None)
    path: str | None = Field(default=None)
    values: list[AnyOf_ParameterWithValuesValues] | None = Field(default=None)
