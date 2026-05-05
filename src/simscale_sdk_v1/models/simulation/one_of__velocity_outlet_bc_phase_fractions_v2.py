from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.outlet_back_flow_pf_values import OutletBackFlowPFValues
from simscale_sdk_v1.models.simulation.outlet_flow_driven_pf import OutletFlowDrivenPF

_ONE_OF__VELOCITY_OUTLET_BC_PHASE_FRACTIONS_V2_VARIANTS: dict[str, type] = {
    "OUTLET_BACK_FLOW_PF_VALUES": OutletBackFlowPFValues,
    "OUTLET_FLOW_DRIVEN_PF": OutletFlowDrivenPF,
}

OneOf_VelocityOutletBCPhaseFractionsV2 = Annotated[
    Union[OutletBackFlowPFValues, OutletFlowDrivenPF],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_OUTLET_BC_PHASE_FRACTIONS_V2_VARIANTS,
        )
    ),
]
