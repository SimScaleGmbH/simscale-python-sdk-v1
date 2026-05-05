from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class HydrostaticPressure(SimScaleModel):
    enable_hydrostatic_pressure: bool | None = Field(
        validation_alias="enableHydrostaticPressure", serialization_alias="enableHydrostaticPressure", default=False
    )
    reference_height: Dimensional_Length | None = Field(
        validation_alias="referenceHeight", serialization_alias="referenceHeight", default=None
    )
