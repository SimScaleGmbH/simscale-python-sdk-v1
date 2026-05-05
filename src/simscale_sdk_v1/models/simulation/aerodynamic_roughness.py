from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class AerodynamicRoughness(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AERODYNAMIC_ROUGHNESS",
        description="Schema name: AerodynamicRoughness",
    )
    surface_roughness: Dimensional_Length | None = Field(
        validation_alias="surfaceRoughness", serialization_alias="surfaceRoughness", default=None
    )
