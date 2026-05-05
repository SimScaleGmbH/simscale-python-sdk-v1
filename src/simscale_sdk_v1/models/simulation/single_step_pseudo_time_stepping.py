from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class SingleStepPseudoTimeStepping(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SINGLE_STEP",
        description="Schema name: SingleStepPseudoTimeStepping",
    )
    static_timesteps: Dimensional_Time | None = Field(
        validation_alias="staticTimesteps", serialization_alias="staticTimesteps", default=None
    )
