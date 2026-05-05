from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OutletFlowDrivenPF(SimScaleModel):
    """Phase fraction values are automatically computed."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTLET_FLOW_DRIVEN_PF",
        description="Phase fraction values are automatically computed.  Schema name: OutletFlowDrivenPF",
    )
