from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.compute_resource_type import ComputeResourceType


class ComputeResource(SimScaleModel):
    """An interval with the estimated compute resources (CPUh or GPUh) required to run the simulation."""

    type_: ComputeResourceType | None = Field(validation_alias="type", serialization_alias="type", default=None)
    value: float | None = Field(default=None)
    interval_min: float | None = Field(validation_alias="intervalMin", serialization_alias="intervalMin", default=None)
    interval_max: float | None = Field(validation_alias="intervalMax", serialization_alias="intervalMax", default=None)
