from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.layer_wall_thermal import LayerWallThermal
from simscale_sdk_v1.models.simulation.no_wall_thermal import NoWallThermal
from simscale_sdk_v1.models.simulation.specific_conductance_wall_thermal import SpecificConductanceWallThermal
from simscale_sdk_v1.models.simulation.total_resistance_wall_thermal import TotalResistanceWallThermal

# This option allows you to model a thin layer resistance on the boundary. Learn more.
_ONE_OF__DERIVED_HEAT_FLUX_WALL_THERMAL_VARIANTS: dict[str, type] = {
    "NO_RESISTANCE": NoWallThermal,
    "TOTAL_RESISTANCE": TotalResistanceWallThermal,
    "SPECIFIC_CONDUCTANCE": SpecificConductanceWallThermal,
    "CONTACT_INTERFACE_MATERIAL": LayerWallThermal,
}

OneOf_DerivedHeatFluxWallThermal = Annotated[
    Union[NoWallThermal, TotalResistanceWallThermal, SpecificConductanceWallThermal, LayerWallThermal],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DERIVED_HEAT_FLUX_WALL_THERMAL_VARIANTS,
        )
    ),
]
