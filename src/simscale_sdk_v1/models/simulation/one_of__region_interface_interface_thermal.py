from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.adiabatic_interface_thermal import AdiabaticInterfaceThermal
from simscale_sdk_v1.models.simulation.contact_interface_material_interface_thermal import (
    ContactInterfaceMaterialInterfaceThermal,
)
from simscale_sdk_v1.models.simulation.coupled_interface_thermal import CoupledInterfaceThermal
from simscale_sdk_v1.models.simulation.specific_conductance_interface_thermal import SpecificConductanceInterfaceThermal
from simscale_sdk_v1.models.simulation.total_resistance_interface_thermal import TotalResistanceInterfaceThermal

_ONE_OF__REGION_INTERFACE_INTERFACE_THERMAL_VARIANTS: dict[str, type] = {
    "COUPLED": CoupledInterfaceThermal,
    "ADIABATIC": AdiabaticInterfaceThermal,
    "TOTAL_RESISTANCE": TotalResistanceInterfaceThermal,
    "SPECIFIC_CONDUCTANCE": SpecificConductanceInterfaceThermal,
    "CONTACT_INTERFACE_MATERIAL": ContactInterfaceMaterialInterfaceThermal,
}

OneOf_RegionInterfaceInterfaceThermal = Annotated[
    Union[
        CoupledInterfaceThermal,
        AdiabaticInterfaceThermal,
        TotalResistanceInterfaceThermal,
        SpecificConductanceInterfaceThermal,
        ContactInterfaceMaterialInterfaceThermal,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__REGION_INTERFACE_INTERFACE_THERMAL_VARIANTS,
        )
    ),
]
