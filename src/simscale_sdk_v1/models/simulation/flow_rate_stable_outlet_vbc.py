from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__flow_rate_stable_outlet_vbc_flow_rate import (
    OneOf_FlowRateStableOutletVBCFlowRate,
)


class FlowRateStableOutletVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLOW_RATE_STABLE_OUTLET_VELOCITY",
        description="Schema name: FlowRateStableOutletVBC",
    )
    flow_rate: OneOf_FlowRateStableOutletVBCFlowRate | None = Field(
        validation_alias="flowRate", serialization_alias="flowRate", default=None
    )
