from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class WallRadiationModel(SimScaleModel):
    emissivity: float | None = Field(
        default=0,
        description="The proportionality factor emissivity defines the type of radiation. The lower bound (0) determining complete reflection and the upper bound (1) defining complete absorption (black body).",
    )
    ambient_temperature: Dimensional_Temperature | None = Field(
        validation_alias="ambientTemperature", serialization_alias="ambientTemperature", default=None
    )
