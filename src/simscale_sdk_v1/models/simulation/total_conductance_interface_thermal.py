from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__electric_conductance import Dimensional_ElectricConductance
from simscale_sdk_v1.models.simulation.dimensional__total_thermal_transmittance import (
    Dimensional_TotalThermalTransmittance,
)


class TotalConductanceInterfaceThermal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_CONDUCTANCE",
        description="Schema name: TotalConductanceInterfaceThermal",
    )
    contact_conductance: Dimensional_TotalThermalTransmittance | None = Field(
        validation_alias="contactConductance", serialization_alias="contactConductance", default=None
    )
    electric_conductance: Dimensional_ElectricConductance | None = Field(
        validation_alias="electricConductance", serialization_alias="electricConductance", default=None
    )
