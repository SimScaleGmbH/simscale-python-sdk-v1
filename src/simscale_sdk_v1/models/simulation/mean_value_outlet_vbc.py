from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__speed import DimensionalFunction_Speed


class MeanValueOutletVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MEAN_VALUE_OUTLET_VELOCITY",
        description="Schema name: MeanValueOutletVBC",
    )
    normal_velocity: DimensionalFunction_Speed | None = Field(
        validation_alias="normalVelocity", serialization_alias="normalVelocity", default=None
    )
