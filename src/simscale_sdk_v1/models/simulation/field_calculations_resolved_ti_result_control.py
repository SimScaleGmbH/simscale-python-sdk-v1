from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.resolved_turbulence_intensity import ResolvedTurbulenceIntensity


class FieldCalculationsResolvedTIResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RESOLVED_TURBULENCE_INTENSITY",
        description="Schema name: FieldCalculationsResolvedTIResultControl",
    )
    name: str | None = Field(default=None)
    result_type: ResolvedTurbulenceIntensity | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
