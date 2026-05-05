from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.angular_rotation import AngularRotation
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class CentrifugalForceBC(SimScaleModel):
    """This is a centrifugal force boundary condition. Each volume element of the selection is loaded with a centrifugal force which is calculated depending on its volume, the density of the assigned material, its distance from the axis of rotation and the defined rotational velocity.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CENTRIFUGAL_FORCE",
        description="This is a centrifugal force boundary condition. Each volume element of the selection is loaded with a centrifugal force which is calculated depending on its volume, the density of the assigned material, its distance from the axis of rotation and the defined rotational velocity.Learn more.  Schema name: CentrifugalForceBC",
    )
    name: str | None = Field(default=None)
    rotation: AngularRotation | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
