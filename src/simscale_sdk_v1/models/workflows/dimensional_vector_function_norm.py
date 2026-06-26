from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalVectorFunctionNorm(SimScaleModel):
    argument: Any | None = Field(
        default=None,
        description="Value model for a dimensional vector.  Resolves to an object node with field `vector` containing Cartesian vector components (`x`, `y`, `z`; as double nodes) and field `unit` (text node).  Note that during resolution, all dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s),",
    )
    value_model_type: str
