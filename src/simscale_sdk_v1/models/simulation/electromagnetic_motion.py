from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__electromagnetic_motion_motion import OneOf_ElectromagneticMotionMotion
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ElectromagneticMotion(SimScaleModel):
    name: str | None = Field(default=None)
    motion_method: Literal["PRESCRIBED", "COMPUTED"] | None = Field(
        validation_alias="motionMethod", serialization_alias="motionMethod", default="PRESCRIBED"
    )
    motion: OneOf_ElectromagneticMotionMotion | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
