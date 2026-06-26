from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value import Value


class AsDimensionalScalarValue(SimScaleModel):
    value_model_type: str
    value: Value | None = Field(default=None)
