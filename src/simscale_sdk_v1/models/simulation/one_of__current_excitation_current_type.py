from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.electromagnetic_current_type_constant import ElectromagneticCurrentTypeConstant
from simscale_sdk_v1.models.simulation.electromagnetic_current_type_sinusoidal import (
    ElectromagneticCurrentTypeSinusoidal,
)
from simscale_sdk_v1.models.simulation.electromagnetic_current_type_table import ElectromagneticCurrentTypeTable

# Constant: Definition of a constant current value. Sinusoidal: Definition of a current that changes sinusoidally with time. Table: Definition of current values at specific time intervals.
_ONE_OF__CURRENT_EXCITATION_CURRENT_TYPE_VARIANTS: dict[str, type] = {
    "CURRENT_TYPE_CONSTANT": ElectromagneticCurrentTypeConstant,
    "CURRENT_TYPE_SINUSOIDAL": ElectromagneticCurrentTypeSinusoidal,
    "CURRENT_TYPE_TABLE": ElectromagneticCurrentTypeTable,
}

OneOf_CurrentExcitationCurrentType = Annotated[
    Union[ElectromagneticCurrentTypeConstant, ElectromagneticCurrentTypeSinusoidal, ElectromagneticCurrentTypeTable],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CURRENT_EXCITATION_CURRENT_TYPE_VARIANTS,
        )
    ),
]
