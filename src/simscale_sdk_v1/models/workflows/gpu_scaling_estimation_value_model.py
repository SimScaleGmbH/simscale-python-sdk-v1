from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GpuScalingEstimationValueModel(SimScaleModel):
    cpus: Any | None = Field(default=None, description="Value model for a list of values. Resolves to a JSON array.")
    gpu_memory: Any | None = Field(
        validation_alias="gpuMemory",
        serialization_alias="gpuMemory",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
