from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__volume_force import Dimensional_VolumeForce


class DistributedIsotropicStiffnessDefinition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISTRIBUTED_ISOTROPIC",
        description="Schema name: DistributedIsotropicStiffnessDefinition",
    )
    distributed: Dimensional_VolumeForce | None = Field(default=None)
