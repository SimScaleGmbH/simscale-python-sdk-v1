from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.boolean_value import BooleanValue


class PairBooleanValueBooleanValue(SimScaleModel):
    first: BooleanValue | None = Field(default=None)
    second: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
