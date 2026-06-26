from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.boolean_value import BooleanValue


class PairBooleanValueMeasurementUnitValue(SimScaleModel):
    first: BooleanValue | None = Field(default=None)
    second: Any | None = Field(
        default=None, description="Value model for a measurement unit value. Resolves to a text JSON node."
    )
