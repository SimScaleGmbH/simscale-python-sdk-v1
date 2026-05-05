from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__volume_force import DimensionalVector_VolumeForce


class DistributedOrthotropicStiffnessDefinition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISTRIBUTED_ORTHOTROPIC",
        description="Schema name: DistributedOrthotropicStiffnessDefinition",
    )
    distributed: DimensionalVector_VolumeForce | None = Field(default=None)
