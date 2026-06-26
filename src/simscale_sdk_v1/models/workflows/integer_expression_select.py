from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.pair_boolean_value_integer_value import PairBooleanValueIntegerValue


class IntegerExpressionSelect(SimScaleModel):
    options: list[PairBooleanValueIntegerValue] | None = Field(default=None)
