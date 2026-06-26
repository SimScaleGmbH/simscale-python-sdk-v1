from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ValueListFunctionIsEmpty(SimScaleModel):
    value_list: Any | None = Field(
        validation_alias="valueList",
        serialization_alias="valueList",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
    value_model_type: str
