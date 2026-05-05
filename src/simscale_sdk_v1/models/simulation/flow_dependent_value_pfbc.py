from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FlowDependentValuePFBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLOW_DEPENDENT_VALUE",
        description="Schema name: FlowDependentValuePFBC",
    )
    lower_bound: float | None = Field(validation_alias="lowerBound", serialization_alias="lowerBound", default=0)
    upper_bound: float | None = Field(validation_alias="upperBound", serialization_alias="upperBound", default=1)
