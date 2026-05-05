from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.marc_external_pressure_type import MarcExternalPressureType


class MarcPressureFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE",
        description="Schema name: MarcPressureFieldSelection",
    )
    pressure_type: MarcExternalPressureType | None = Field(
        validation_alias="pressureType", serialization_alias="pressureType", default=None
    )
