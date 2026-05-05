from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_gradient_psbc import FixedGradientPSBC
from simscale_sdk_v1.models.simulation.fixed_value_psbc import FixedValuePSBC
from simscale_sdk_v1.models.simulation.inlet_outlet_psbc import InletOutletPSBC
from simscale_sdk_v1.models.simulation.symmetry_psbc import SymmetryPSBC
from simscale_sdk_v1.models.simulation.zero_gradient_psbc import ZeroGradientPSBC

_ONE_OF__CUSTOM_FLUID_BC_PASSIVE_SCALARS_VARIANTS: dict[str, type] = {
    "FIXED_GRADIENT": FixedGradientPSBC,
    "FIXED_VALUE": FixedValuePSBC,
    "INLET_OUTLET": InletOutletPSBC,
    "ZERO_GRADIENT": ZeroGradientPSBC,
    "SYMMETRY": SymmetryPSBC,
}

OneOf_CustomFluidBCPassiveScalars = Annotated[
    Union[FixedGradientPSBC, FixedValuePSBC, InletOutletPSBC, ZeroGradientPSBC, SymmetryPSBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_PASSIVE_SCALARS_VARIANTS,
        )
    ),
]
