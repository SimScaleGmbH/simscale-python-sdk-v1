from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.current_inflow_ebc import CurrentInflowEBC
from simscale_sdk_v1.models.simulation.current_outflow_ebc import CurrentOutflowEBC
from simscale_sdk_v1.models.simulation.fixed_electric_potential_ebc import FixedElectricPotentialEBC
from simscale_sdk_v1.models.simulation.no_current_ebc import NoCurrentEBC

_ONE_OF__WALL_BC_ELECTRIC_BOUNDARY_CONDITION_VARIANTS: dict[str, type] = {
    "NO_CURRENT": NoCurrentEBC,
    "CURRENT_INFLOW": CurrentInflowEBC,
    "CURRENT_OUTFLOW": CurrentOutflowEBC,
    "FIXED_ELECTRIC_POTENTIAL": FixedElectricPotentialEBC,
}

OneOf_WallBCElectricBoundaryCondition = Annotated[
    Union[NoCurrentEBC, CurrentInflowEBC, CurrentOutflowEBC, FixedElectricPotentialEBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WALL_BC_ELECTRIC_BOUNDARY_CONDITION_VARIANTS,
        )
    ),
]
