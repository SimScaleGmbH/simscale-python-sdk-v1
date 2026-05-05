from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.vector_field import VectorField


class Displacement(SimScaleModel):
    field: VectorField
    scale_factor: float = Field(validation_alias="scaleFactor", serialization_alias="scaleFactor", default=1.0)
