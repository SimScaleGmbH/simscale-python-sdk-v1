from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.compute_resource_type import ComputeResourceType


class MeshOperationComputeResource(SimScaleModel):
    """The actual compute resources (CPUh only) consumed by the mesh operation."""

    type_: ComputeResourceType | None = Field(validation_alias="type", serialization_alias="type", default=None)
    value: float | None = Field(default=None)
