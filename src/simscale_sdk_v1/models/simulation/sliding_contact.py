from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__sliding_contact_position_tolerance import (
    OneOf_SlidingContactPositionTolerance,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SlidingContact(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SLIDING_CONTACT",
        description="Schema name: SlidingContact",
    )
    name: str | None = Field(default=None)
    enable_heat_transfer: Literal["YES", "NO", "HEAT_TRANSFER_ONLY"] | None = Field(
        validation_alias="enableHeatTransfer", serialization_alias="enableHeatTransfer", default="YES"
    )
    position_tolerance: OneOf_SlidingContactPositionTolerance | None = Field(
        validation_alias="positionTolerance", serialization_alias="positionTolerance", default=None
    )
    master_topological_reference: TopologicalReference | None = Field(
        validation_alias="masterTopologicalReference", serialization_alias="masterTopologicalReference", default=None
    )
    slave_topological_reference: TopologicalReference | None = Field(
        validation_alias="slaveTopologicalReference", serialization_alias="slaveTopologicalReference", default=None
    )
