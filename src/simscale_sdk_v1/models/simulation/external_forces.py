from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__force import DimensionalFunction_Force
from simscale_sdk_v1.models.simulation.spring_damper import SpringDamper


class ExternalForces(SimScaleModel):
    enable_gravity: bool | None = Field(
        validation_alias="enableGravity",
        serialization_alias="enableGravity",
        default=False,
        description="Whether the weight of the body acts on the motion. Only the projection of the weight onto the motion axis has an effect.The magnitude and direction of gravity are defined once under simulation control, so every motion in the simulation shares the same gravity.",
    )
    spring_damper: SpringDamper | None = Field(
        validation_alias="springDamper", serialization_alias="springDamper", default=None
    )
    external_force: DimensionalFunction_Force | None = Field(
        validation_alias="externalForce", serialization_alias="externalForce", default=None
    )
