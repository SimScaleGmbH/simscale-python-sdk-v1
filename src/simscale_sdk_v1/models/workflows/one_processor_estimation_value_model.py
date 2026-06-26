from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.one_gpu_estimation_value_model import OneGpuEstimationValueModel


class OneProcessorEstimationValueModel(SimScaleModel):
    gpu_estimation: OneGpuEstimationValueModel | None = Field(
        validation_alias="gpuEstimation", serialization_alias="gpuEstimation", default=None
    )
    memory_in_mebibytes: Any | None = Field(
        validation_alias="memoryInMebibytes",
        serialization_alias="memoryInMebibytes",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    storage_in_mebibytes: Any | None = Field(
        validation_alias="storageInMebibytes",
        serialization_alias="storageInMebibytes",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    time_in_seconds: Any | None = Field(
        validation_alias="timeInSeconds",
        serialization_alias="timeInSeconds",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    time_in_seconds_by_arch: Any | None = Field(
        validation_alias="timeInSecondsByArch",
        serialization_alias="timeInSecondsByArch",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
    time_in_seconds_by_gpu_arch: Any | None = Field(
        validation_alias="timeInSecondsByGpuArch",
        serialization_alias="timeInSecondsByGpuArch",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
    time_in_seconds_by_gpu_arch_and_model: Any | None = Field(
        validation_alias="timeInSecondsByGpuArchAndModel",
        serialization_alias="timeInSecondsByGpuArchAndModel",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
