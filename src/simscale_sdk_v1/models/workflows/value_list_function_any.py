from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ValueListFunctionAny(SimScaleModel):
    value_model_type: str
    criteria: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
    iterator_reference: Any | None = Field(
        validation_alias="iteratorReference",
        serialization_alias="iteratorReference",
        default=None,
        description="Iterator reference for processing collections.",
    )
    value_list: Any | None = Field(
        validation_alias="valueList",
        serialization_alias="valueList",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
