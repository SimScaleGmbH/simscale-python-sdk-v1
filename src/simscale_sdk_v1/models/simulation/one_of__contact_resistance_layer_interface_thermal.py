from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.specific_resistance_interface_thermal import SpecificResistanceInterfaceThermal
from simscale_sdk_v1.models.simulation.total_resistance_interface_thermal import TotalResistanceInterfaceThermal

_ONE_OF__CONTACT_RESISTANCE_LAYER_INTERFACE_THERMAL_VARIANTS: dict[str, type] = {
    "TOTAL_RESISTANCE": TotalResistanceInterfaceThermal,
    "SPECIFIC_RESISTANCE": SpecificResistanceInterfaceThermal,
}

OneOf_ContactResistanceLayerInterfaceThermal = Annotated[
    Union[TotalResistanceInterfaceThermal, SpecificResistanceInterfaceThermal],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONTACT_RESISTANCE_LAYER_INTERFACE_THERMAL_VARIANTS,
        )
    ),
]
