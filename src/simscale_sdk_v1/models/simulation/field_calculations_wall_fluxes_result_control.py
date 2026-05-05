from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.wall_shear_stress_result_type import WallShearStressResultType


class FieldCalculationsWallFluxesResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_FLUXES",
        description="Schema name: FieldCalculationsWallFluxesResultControl",
    )
    name: str | None = Field(default=None)
    result_type: WallShearStressResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
