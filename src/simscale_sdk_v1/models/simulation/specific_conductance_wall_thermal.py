from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__thermal_transmittance import Dimensional_ThermalTransmittance


class SpecificConductanceWallThermal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIFIC_CONDUCTANCE",
        description="Schema name: SpecificConductanceWallThermal",
    )
    contact_conductance: Dimensional_ThermalTransmittance | None = Field(
        validation_alias="contactConductance", serialization_alias="contactConductance", default=None
    )
