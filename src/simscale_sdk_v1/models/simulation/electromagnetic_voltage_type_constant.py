from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__electric_potential import Dimensional_ElectricPotential


class ElectromagneticVoltageTypeConstant(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLTAGE_TYPE_CONSTANT",
        description="Schema name: ElectromagneticVoltageTypeConstant",
    )
    value: Dimensional_ElectricPotential | None = Field(default=None)
