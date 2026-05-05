from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class SetValuePositionTolerance(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SET_VALUE",
        description="Schema name: SetValuePositionTolerance",
    )
    tolerance: Dimensional_Length | None = Field(default=None)
