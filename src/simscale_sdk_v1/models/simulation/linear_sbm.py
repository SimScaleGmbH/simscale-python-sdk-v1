from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed


class LinearSBM(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LINEAR_MOTION",
        description="Schema name: LinearSBM",
    )
    name: str | None = Field(default=None)
    velocity: DimensionalVector_Speed | None = Field(default=None)
