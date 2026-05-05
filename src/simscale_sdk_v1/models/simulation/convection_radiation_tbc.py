from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.wall_convection_model import WallConvectionModel
from simscale_sdk_v1.models.simulation.wall_radiation_model import WallRadiationModel


class ConvectionRadiationTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONVECTIVE_RADIATIVE_HEAT_TRANSFER",
        description="Schema name: ConvectionRadiationTBC",
    )
    convection: WallConvectionModel | None = Field(default=None)
    radiation: WallRadiationModel | None = Field(default=None)
