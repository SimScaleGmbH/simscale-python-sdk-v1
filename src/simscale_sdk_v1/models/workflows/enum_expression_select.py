from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.pair_boolean_value_enum_value import PairBooleanValueEnumValue


class EnumExpressionSelect(SimScaleModel):
    options: list[PairBooleanValueEnumValue] | None = Field(default=None)
    value_model_type: str
