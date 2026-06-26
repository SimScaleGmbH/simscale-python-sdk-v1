from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.pair_boolean_value_value_list_value import PairBooleanValueValueListValue


class ValueListExpressionSelect(SimScaleModel):
    options: list[PairBooleanValueValueListValue] | None = Field(default=None)
    value_model_type: str
