from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector_function__pressure import DimensionalVectorFunction_Pressure
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SurfaceLoadBC(SimScaleModel):
    """This is a surface load boundary condition representing a distributed load on the selection. It is applied as surface traction in the global coordinate system.Important remarks: The applied total force depends on the surface area of the selectionLearn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_LOAD",
        description="This is a surface load boundary condition representing a distributed load on the selection. It is applied as surface traction in the global coordinate system.Important remarks: The applied total force depends on the surface area of the selectionLearn more.  Schema name: SurfaceLoadBC",
    )
    name: str | None = Field(default=None)
    load: DimensionalVectorFunction_Pressure | None = Field(default=None)
    scaling: DimensionalFunction_Dimensionless | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
