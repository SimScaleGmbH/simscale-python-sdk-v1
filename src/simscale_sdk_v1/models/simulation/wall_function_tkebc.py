from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class WallFunctionTKEBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_FUNCTION",
        description="Schema name: WallFunctionTKEBC",
    )
    wall_roughness: bool | None = Field(
        validation_alias="wallRoughness", serialization_alias="wallRoughness", default=False
    )
    roughness_height: Dimensional_Length | None = Field(
        validation_alias="roughnessHeight", serialization_alias="roughnessHeight", default=None
    )
    roughness_constant: float | None = Field(
        validation_alias="roughnessConstant", serialization_alias="roughnessConstant", default=0.5
    )
