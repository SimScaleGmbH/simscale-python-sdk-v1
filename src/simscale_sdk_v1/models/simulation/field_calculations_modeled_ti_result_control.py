from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.modeled_turbulence_intensity import ModeledTurbulenceIntensity


class FieldCalculationsModeledTIResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MODELED_TURBULENCE_INTENSITY",
        description="Schema name: FieldCalculationsModeledTIResultControl",
    )
    name: str | None = Field(default=None)
    result_type: ModeledTurbulenceIntensity | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
