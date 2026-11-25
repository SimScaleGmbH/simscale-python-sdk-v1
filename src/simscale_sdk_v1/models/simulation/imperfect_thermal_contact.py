from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__thermal_transmittance import Dimensional_ThermalTransmittance


class ImperfectThermalContact(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="IMPERFECT",
        description="Schema name: ImperfectThermalContact",
    )
    marc_contact_conductance: Dimensional_ThermalTransmittance | None = Field(
        validation_alias="marcContactConductance", serialization_alias="marcContactConductance", default=None
    )
