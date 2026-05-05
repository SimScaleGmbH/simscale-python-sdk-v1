from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class MeanValuePBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_MEAN",
        description="Schema name: MeanValuePBC",
    )
    value: Dimensional_Pressure | None = Field(default=None)
