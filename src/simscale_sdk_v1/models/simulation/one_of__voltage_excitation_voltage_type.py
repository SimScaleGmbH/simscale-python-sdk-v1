from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_constant import ElectromagneticVoltageTypeConstant
from simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_sinusoidal import (
    ElectromagneticVoltageTypeSinusoidal,
)
from simscale_sdk_v1.models.simulation.electromagnetic_voltage_type_table import ElectromagneticVoltageTypeTable

# Constant: Definition of a constant voltage value. Sinusoidal: Definition of a voltage that changes sinusoidally with time. Table: Definition of voltage values at specific time intervals.
_ONE_OF__VOLTAGE_EXCITATION_VOLTAGE_TYPE_VARIANTS: dict[str, type] = {
    "VOLTAGE_TYPE_CONSTANT": ElectromagneticVoltageTypeConstant,
    "VOLTAGE_TYPE_SINUSOIDAL": ElectromagneticVoltageTypeSinusoidal,
    "VOLTAGE_TYPE_TABLE": ElectromagneticVoltageTypeTable,
}

OneOf_VoltageExcitationVoltageType = Annotated[
    Union[ElectromagneticVoltageTypeConstant, ElectromagneticVoltageTypeSinusoidal, ElectromagneticVoltageTypeTable],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VOLTAGE_EXCITATION_VOLTAGE_TYPE_VARIANTS,
        )
    ),
]
