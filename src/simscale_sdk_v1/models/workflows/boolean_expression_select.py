from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.pair_boolean_value_boolean_value import PairBooleanValueBooleanValue


class BooleanExpressionSelect(SimScaleModel):
    options: list[PairBooleanValueBooleanValue] | None = Field(default=None)
