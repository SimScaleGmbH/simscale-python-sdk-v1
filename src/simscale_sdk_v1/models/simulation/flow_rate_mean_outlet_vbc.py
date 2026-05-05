from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__flow_rate_mean_outlet_vbc_flow_rate import (
    OneOf_FlowRateMeanOutletVBCFlowRate,
)


class FlowRateMeanOutletVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLOW_RATE_MEAN_OUTLET_VELOCITY",
        description="Schema name: FlowRateMeanOutletVBC",
    )
    flow_rate: OneOf_FlowRateMeanOutletVBCFlowRate | None = Field(
        validation_alias="flowRate", serialization_alias="flowRate", default=None
    )
