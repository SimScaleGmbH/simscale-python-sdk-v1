from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.resolved_turbulent_kinetic_energy import ResolvedTurbulentKineticEnergy


class FieldCalculationsResolvedTKEResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RESOLVED_TURBULENT_KINETIC_ENERGY",
        description="Schema name: FieldCalculationsResolvedTKEResultControl",
    )
    name: str | None = Field(default=None)
    result_type: ResolvedTurbulentKineticEnergy | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
