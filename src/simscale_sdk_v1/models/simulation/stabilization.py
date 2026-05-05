from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.field_limits import FieldLimits


class Stabilization(SimScaleModel):
    field_limits: FieldLimits | None = Field(
        validation_alias="fieldLimits", serialization_alias="fieldLimits", default=None
    )
