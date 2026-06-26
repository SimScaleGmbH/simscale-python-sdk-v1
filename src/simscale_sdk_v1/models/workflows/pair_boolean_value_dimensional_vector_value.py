from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.boolean_value import BooleanValue


class PairBooleanValueDimensionalVectorValue(SimScaleModel):
    first: BooleanValue | None = Field(default=None)
    second: Any | None = Field(
        default=None,
        description="Value model for a dimensional vector.  Resolves to an object node with field `vector` containing Cartesian vector components (`x`, `y`, `z`; as double nodes) and field `unit` (text node).  Note that during resolution, all dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s),",
    )
