from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__acceleration import DimensionalFunction_Acceleration
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class SolidModel(SimScaleModel):
    geometric_behavior: Literal["LINEAR", "NONLINEAR"] | None = Field(
        validation_alias="geometricBehavior", serialization_alias="geometricBehavior", default="NONLINEAR"
    )
    magnitude: DimensionalFunction_Acceleration | None = Field(default=None)
    e: DimensionalVector_Length | None = Field(default=None)
