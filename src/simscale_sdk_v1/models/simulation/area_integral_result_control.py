from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__area_integral_result_control_write_control import (
    OneOf_AreaIntegralResultControlWriteControl,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class AreaIntegralResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AREA_INTEGRAL",
        description="Schema name: AreaIntegralResultControl",
    )
    name: str | None = Field(default=None)
    write_control: OneOf_AreaIntegralResultControlWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
