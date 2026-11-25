from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class TravelDistance(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TRAVEL_DISTANCE",
        description="Schema name: TravelDistance",
    )
    forward_travel: Dimensional_Length | None = Field(
        validation_alias="forwardTravel", serialization_alias="forwardTravel", default=None
    )
    backward_travel: Dimensional_Length | None = Field(
        validation_alias="backwardTravel", serialization_alias="backwardTravel", default=None
    )
