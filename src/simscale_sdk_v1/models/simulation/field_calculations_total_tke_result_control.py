from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.total_turbulent_kinetic_energy import TotalTurbulentKineticEnergy


class FieldCalculationsTotalTKEResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_TURBULENT_KINETIC_ENERGY",
        description="Schema name: FieldCalculationsTotalTKEResultControl",
    )
    name: str | None = Field(default=None)
    result_type: TotalTurbulentKineticEnergy | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
