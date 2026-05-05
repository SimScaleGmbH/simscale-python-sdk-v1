from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of_ami_rotating_zone_motion_type import OneOf_AMIRotatingZoneMotionType
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class AMIRotatingZone(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ARBITRARY_MESH_INTERFACE",
        description="Schema name: AMIRotatingZone",
    )
    name: str | None = Field(default=None)
    motion_type: OneOf_AMIRotatingZoneMotionType | None = Field(
        validation_alias="motionType", serialization_alias="motionType", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
