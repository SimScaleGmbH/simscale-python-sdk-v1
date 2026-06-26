from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.gpu_scaling_estimation_value_model import GpuScalingEstimationValueModel


class ScalingEstimationValueModel(SimScaleModel):
    gpu_scaling: GpuScalingEstimationValueModel | None = Field(
        validation_alias="gpuScaling", serialization_alias="gpuScaling", default=None
    )
    memory: Any | None = Field(default=None, description="Value model for a list of values. Resolves to a JSON array.")
    speed_up: Any | None = Field(
        validation_alias="speedUp",
        serialization_alias="speedUp",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
    storage: Any | None = Field(default=None, description="Value model for a list of values. Resolves to a JSON array.")
