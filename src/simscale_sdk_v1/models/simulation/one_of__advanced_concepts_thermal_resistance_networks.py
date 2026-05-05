from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.star_thermal_resistance_network import StarThermalResistanceNetwork
from simscale_sdk_v1.models.simulation.two_resistor_network import TwoResistorNetwork

_ONE_OF__ADVANCED_CONCEPTS_THERMAL_RESISTANCE_NETWORKS_VARIANTS: dict[str, type] = {
    "STAR_NETWORK": StarThermalResistanceNetwork,
    "TWO_RESISTOR_NETWORK": TwoResistorNetwork,
}

OneOf_AdvancedConceptsThermalResistanceNetworks = Annotated[
    Union[StarThermalResistanceNetwork, TwoResistorNetwork],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_THERMAL_RESISTANCE_NETWORKS_VARIANTS,
        )
    ),
]
