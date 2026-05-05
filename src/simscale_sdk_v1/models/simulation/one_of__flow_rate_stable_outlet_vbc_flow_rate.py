from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.mass_flow import MassFlow
from simscale_sdk_v1.models.simulation.volumetric_flow import VolumetricFlow

_ONE_OF__FLOW_RATE_STABLE_OUTLET_VBC_FLOW_RATE_VARIANTS: dict[str, type] = {
    "MASS": MassFlow,
    "VOLUMETRIC": VolumetricFlow,
}

OneOf_FlowRateStableOutletVBCFlowRate = Annotated[
    Union[MassFlow, VolumetricFlow],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLOW_RATE_STABLE_OUTLET_VBC_FLOW_RATE_VARIANTS,
        )
    ),
]
