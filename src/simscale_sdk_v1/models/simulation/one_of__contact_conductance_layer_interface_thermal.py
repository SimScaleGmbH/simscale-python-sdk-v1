from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.specific_conductance_interface_thermal import SpecificConductanceInterfaceThermal
from simscale_sdk_v1.models.simulation.total_conductance_interface_thermal import TotalConductanceInterfaceThermal

_ONE_OF__CONTACT_CONDUCTANCE_LAYER_INTERFACE_THERMAL_VARIANTS: dict[str, type] = {
    "SPECIFIC_CONDUCTANCE": SpecificConductanceInterfaceThermal,
    "TOTAL_CONDUCTANCE": TotalConductanceInterfaceThermal,
}

OneOf_ContactConductanceLayerInterfaceThermal = Annotated[
    Union[SpecificConductanceInterfaceThermal, TotalConductanceInterfaceThermal],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CONTACT_CONDUCTANCE_LAYER_INTERFACE_THERMAL_VARIANTS,
        )
    ),
]
