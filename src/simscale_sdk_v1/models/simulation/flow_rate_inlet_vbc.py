from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__flow_rate_inlet_vbc_flow_rate import OneOf_FlowRateInletVBCFlowRate


class FlowRateInletVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLOW_RATE_INLET_VELOCITY",
        description="Schema name: FlowRateInletVBC",
    )
    flow_rate: OneOf_FlowRateInletVBCFlowRate | None = Field(
        validation_alias="flowRate", serialization_alias="flowRate", default=None
    )
