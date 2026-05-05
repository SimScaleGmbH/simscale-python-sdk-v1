from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__speed import Dimensional_Speed


class OutletMeanPhaseVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTLET_MEAN_PHASE",
        description="Schema name: OutletMeanPhaseVBC",
    )
    phase: Literal["PHASE_0", "PHASE_1"] | None = Field(default="PHASE_1")
    mean_velocity: Dimensional_Speed | None = Field(
        validation_alias="meanVelocity", serialization_alias="meanVelocity", default=None
    )
