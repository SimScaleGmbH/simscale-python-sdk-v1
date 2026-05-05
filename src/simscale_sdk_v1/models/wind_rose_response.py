from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.wind_rose import WindRose


class WindRoseResponse(SimScaleModel):
    """Wrapper containing WindRose schema"""

    wind_rose: WindRose = Field(validation_alias="windRose", serialization_alias="windRose")
