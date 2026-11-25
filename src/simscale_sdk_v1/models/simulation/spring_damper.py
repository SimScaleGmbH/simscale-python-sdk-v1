from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__damping import Dimensional_Damping
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__stiffness import Dimensional_Stiffness


class SpringDamper(SimScaleModel):
    stiffness: Dimensional_Stiffness | None = Field(default=None)
    spring_offset: Dimensional_Length | None = Field(
        validation_alias="springOffset", serialization_alias="springOffset", default=None
    )
    damping_factor: Dimensional_Damping | None = Field(
        validation_alias="dampingFactor", serialization_alias="dampingFactor", default=None
    )
