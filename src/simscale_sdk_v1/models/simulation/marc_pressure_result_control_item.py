from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.external_pressure import ExternalPressure


class MarcPressureResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE",
        description="Schema name: MarcPressureResultControlItem",
    )
    name: str | None = Field(default=None)
    pressure_type: ExternalPressure | None = Field(
        validation_alias="pressureType", serialization_alias="pressureType", default=None
    )
