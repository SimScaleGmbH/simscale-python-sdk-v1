from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_value_pfbc import FixedValuePFBC
from simscale_sdk_v1.models.simulation.flow_dependent_value_pfbc import FlowDependentValuePFBC

# Please choose a boundary condition for phase fraction (alpha).
_ONE_OF__VELOCITY_OUTLET_BC_PHASE_FRACTION_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValuePFBC,
    "FLOW_DEPENDENT_VALUE": FlowDependentValuePFBC,
}

OneOf_VelocityOutletBCPhaseFraction = Annotated[
    Union[FixedValuePFBC, FlowDependentValuePFBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_OUTLET_BC_PHASE_FRACTION_VARIANTS,
        )
    ),
]
