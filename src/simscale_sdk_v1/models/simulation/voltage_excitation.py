from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__electric_potential import Dimensional_ElectricPotential
from simscale_sdk_v1.models.simulation.dimensional__electric_resistance import Dimensional_ElectricResistance
from simscale_sdk_v1.models.simulation.one_of__voltage_excitation_voltage_type import OneOf_VoltageExcitationVoltageType


class VoltageExcitation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLTAGE_EXCITATION",
        description="Schema name: VoltageExcitation",
    )
    voltage_type: OneOf_VoltageExcitationVoltageType | None = Field(
        validation_alias="voltageType", serialization_alias="voltageType", default=None
    )
    voltage_rms: Dimensional_ElectricPotential | None = Field(
        validation_alias="voltageRMS", serialization_alias="voltageRMS", default=None
    )
    voltage_phase: Dimensional_Angle | None = Field(
        validation_alias="voltagePhase", serialization_alias="voltagePhase", default=None
    )
    additional_resistance: Dimensional_ElectricResistance | None = Field(
        validation_alias="additionalResistance", serialization_alias="additionalResistance", default=None
    )
