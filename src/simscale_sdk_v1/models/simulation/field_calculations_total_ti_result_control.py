from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.total_turbulence_intensity import TotalTurbulenceIntensity


class FieldCalculationsTotalTIResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_TURBULENCE_INTENSITY",
        description="Schema name: FieldCalculationsTotalTIResultControl",
    )
    name: str | None = Field(default=None)
    result_type: TotalTurbulenceIntensity | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
