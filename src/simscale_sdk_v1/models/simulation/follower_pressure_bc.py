from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FollowerPressureBC(SimScaleModel):
    """In contrast to ordinary pressure, the follower pressure boundary condition is applied normal to the surface of all face elements in the deformed state. This is a nonlinear boundary condition as the update of the geometry is required. In a linear analysis it becomes a simple pressure boundary condition.The following conditions are taken into account: The current deformed state of the surface.Any changes in the direction of the normals of assigned entities.Changes in the surface area of the assigned faces.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FOLLOWER_PRESSURE",
        description="In contrast to ordinary pressure, the follower pressure boundary condition is applied normal to the surface of all face elements in the deformed state. This is a nonlinear boundary condition as the update of the geometry is required. In a linear analysis it becomes a simple pressure boundary condition.The following conditions are taken into account: The current deformed state of the surface.Any changes in the direction of the normals of assigned entities.Changes in the surface area of the assigned faces.Learn more.  Schema name: FollowerPressureBC",
    )
    name: str | None = Field(default=None)
    pressure: DimensionalFunction_Pressure | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
