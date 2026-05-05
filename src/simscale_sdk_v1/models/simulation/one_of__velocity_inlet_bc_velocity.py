from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_magnitude_vbc import FixedMagnitudeVBC
from simscale_sdk_v1.models.simulation.fixed_value_vbc import FixedValueVBC
from simscale_sdk_v1.models.simulation.flow_rate_inlet_vbc import FlowRateInletVBC
from simscale_sdk_v1.models.simulation.flow_rate_mean_inlet_vbc import FlowRateMeanInletVBC
from simscale_sdk_v1.models.simulation.freestream_vbc import FreestreamVBC
from simscale_sdk_v1.models.simulation.mean_value_vbc import MeanValueVBC

# Please choose the type of velocity boundary condition. Learn more.
_ONE_OF__VELOCITY_INLET_BC_VELOCITY_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValueVBC,
    "FIXED_MEAN": MeanValueVBC,
    "FIXED_VALUE_NO_EXPRESSION": FixedMagnitudeVBC,
    "FLOW_RATE_INLET_VELOCITY": FlowRateInletVBC,
    "FLOW_RATE_MEAN_INLET_VELOCITY": FlowRateMeanInletVBC,
    "FREESTREAM": FreestreamVBC,
}

OneOf_VelocityInletBCVelocity = Annotated[
    Union[FixedValueVBC, MeanValueVBC, FixedMagnitudeVBC, FlowRateInletVBC, FlowRateMeanInletVBC, FreestreamVBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__VELOCITY_INLET_BC_VELOCITY_VARIANTS,
        )
    ),
]
