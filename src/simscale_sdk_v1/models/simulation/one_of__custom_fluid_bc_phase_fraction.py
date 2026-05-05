from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.constant_contact_angle_pfbc import ConstantContactAnglePFBC
from simscale_sdk_v1.models.simulation.dynamic_contact_angle_pfbc import DynamicContactAnglePFBC
from simscale_sdk_v1.models.simulation.fixed_gradient_pfbc import FixedGradientPFBC
from simscale_sdk_v1.models.simulation.fixed_value_pfbc import FixedValuePFBC
from simscale_sdk_v1.models.simulation.flow_dependent_value_pfbc import FlowDependentValuePFBC
from simscale_sdk_v1.models.simulation.inlet_outlet_pfbc import InletOutletPFBC
from simscale_sdk_v1.models.simulation.symmetry_pfbc import SymmetryPFBC
from simscale_sdk_v1.models.simulation.zero_gradient_pfbc import ZeroGradientPFBC

# Please choose a boundary condition for phase fraction (alpha).
_ONE_OF__CUSTOM_FLUID_BC_PHASE_FRACTION_VARIANTS: dict[str, type] = {
    "CONSTANT_CONTACT_ANGLE": ConstantContactAnglePFBC,
    "DYNAMIC_CONTACT_ANGLE": DynamicContactAnglePFBC,
    "FIXED_GRADIENT": FixedGradientPFBC,
    "FIXED_VALUE": FixedValuePFBC,
    "FLOW_DEPENDENT_VALUE": FlowDependentValuePFBC,
    "INLET_OUTLET": InletOutletPFBC,
    "ZERO_GRADIENT": ZeroGradientPFBC,
    "SYMMETRY": SymmetryPFBC,
}

OneOf_CustomFluidBCPhaseFraction = Annotated[
    Union[
        ConstantContactAnglePFBC,
        DynamicContactAnglePFBC,
        FixedGradientPFBC,
        FixedValuePFBC,
        FlowDependentValuePFBC,
        InletOutletPFBC,
        ZeroGradientPFBC,
        SymmetryPFBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_PHASE_FRACTION_VARIANTS,
        )
    ),
]
