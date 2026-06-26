from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value import Value


class AsValueList(SimScaleModel):
    value_model_type: str
    element_model: Value | None = Field(
        validation_alias="elementModel", serialization_alias="elementModel", default=None
    )
    value: Value | None = Field(default=None)
