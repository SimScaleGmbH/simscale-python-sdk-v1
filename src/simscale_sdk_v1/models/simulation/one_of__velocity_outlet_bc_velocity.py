from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_value_vbc import FixedValueVBC
from simscale_sdk_v1.models.simulation.flow_rate_mean_outlet_vbc import FlowRateMeanOutletVBC
from simscale_sdk_v1.models.simulation.flow_rate_outlet_vbc import FlowRateOutletVBC
from simscale_sdk_v1.models.simulation.flow_rate_stable_outlet_vbc import FlowRateStableOutletVBC
from simscale_sdk_v1.models.simulation.freestream_vbc import FreestreamVBC
from simscale_sdk_v1.models.simulation.mean_value_outlet_vbc import MeanValueOutletVBC
from simscale_sdk_v1.models.simulation.mean_value_vbc import MeanValueVBC
from simscale_sdk_v1.models.simulation.outlet_mean_phase_vbc import OutletMeanPhaseVBC

# Please choose the type of velocity boundary condition. Learn more.
_ONE_OF__VELOCITY_OUTLET_BC_VELOCITY_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValueVBC,
    "FIXED_MEAN": MeanValueVBC,
    "FREESTREAM": FreestreamVBC,
    "OUTLET_MEAN_PHASE": OutletMeanPhaseVBC,
    "FLOW_RATE_OUTLET_VELOCITY": FlowRateOutletVBC,
    "FLOW_RATE_MEAN_OUTLET_VELOCITY": FlowRateMeanOutletVBC,
    "FLOW_RATE_STABLE_OUTLET_VELOCITY": FlowRateStableOutletVBC,
    "MEAN_VALUE_OUTLET_VELOCITY": MeanValueOutletVBC,
}

OneOf_VelocityOutletBCVelocity = Annotated[
    Union[
        FixedValueVBC,
        MeanValueVBC,
        FreestreamVBC,
        OutletMeanPhaseVBC,
        FlowRateOutletVBC,
        FlowRateMeanOutletVBC,
        FlowRateStableOutletVBC,
        MeanValueOutletVBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_OUTLET_BC_VELOCITY_VARIANTS,
        )
    ),
]
