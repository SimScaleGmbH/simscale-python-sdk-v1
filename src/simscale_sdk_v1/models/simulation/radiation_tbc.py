from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.wall_radiation_model import WallRadiationModel


class RadiationTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RADIATIVE_HEAT_TRANSFER",
        description="Schema name: RadiationTBC",
    )
    radiation: WallRadiationModel | None = Field(default=None)
