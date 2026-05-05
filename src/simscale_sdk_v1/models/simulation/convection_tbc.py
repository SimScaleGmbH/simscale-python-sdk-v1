from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.wall_convection_model import WallConvectionModel


class ConvectionTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONVECTIVE_HEAT_TRANSFER",
        description="Schema name: ConvectionTBC",
    )
    convection: WallConvectionModel | None = Field(default=None)
