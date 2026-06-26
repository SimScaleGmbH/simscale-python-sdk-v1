from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OneGpuEstimationValueModel(SimScaleModel):
    cpus: Any | None = Field(
        default=None, description="Value model for a 64-bit signed integer value. Resolves to a long JSON node."
    )
    gpu_memory_in_mebibytes: Any | None = Field(
        validation_alias="gpuMemoryInMebibytes",
        serialization_alias="gpuMemoryInMebibytes",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
