from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.pair_boolean_value_real_value import PairBooleanValueRealValue


class RealExpressionSelect(SimScaleModel):
    options: list[PairBooleanValueRealValue] | None = Field(default=None)
