from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ResourceUsage(SimScaleModel):
    """Resource usage amount in core-seconds."""

    cpu_core_seconds: int | None = Field(
        validation_alias="cpuCoreSeconds", serialization_alias="cpuCoreSeconds", default=None
    )
    gpu_core_seconds: int | None = Field(
        validation_alias="gpuCoreSeconds", serialization_alias="gpuCoreSeconds", default=None
    )
