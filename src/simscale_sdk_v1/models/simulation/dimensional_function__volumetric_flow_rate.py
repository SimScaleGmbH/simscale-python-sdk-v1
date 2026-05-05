from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__volumetric_flow_rate_value import (
    OneOf_DimensionalFunction_VolumetricFlowRateValue,
)


class DimensionalFunction_VolumetricFlowRate(SimScaleModel):
    value: OneOf_DimensionalFunction_VolumetricFlowRateValue | None = Field(default=None)
    unit: Literal[
        "m³/s",
        "in³/s",
        "m³/min",
        "m³/h",
        "mm³/s",
        "mm³/min",
        "mm³/h",
        "cm³/s",
        "cm³/min",
        "cm³/h",
        "l/s",
        "l/min",
        "l/h",
        "in³/min",
        "in³/h",
        "ft³/s",
        "ft³/min",
        "ft³/h",
        "gal/min",
        "gal/h",
        "gal/s",
    ]
