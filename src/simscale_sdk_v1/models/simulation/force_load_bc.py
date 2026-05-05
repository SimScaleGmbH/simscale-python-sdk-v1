from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector_function__force import DimensionalVectorFunction_Force
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ForceLoadBC(SimScaleModel):
    """This is a force boundary condition representing a distributed force on the selection. The total force is defined in the global coordinate system and each element of the assignment is loaded with a surface traction depending on the area of the element.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FORCE_LOAD",
        description="This is a force boundary condition representing a distributed force on the selection. The total force is defined in the global coordinate system and each element of the assignment is loaded with a surface traction depending on the area of the element.Learn more.  Schema name: ForceLoadBC",
    )
    name: str | None = Field(default=None)
    force: DimensionalVectorFunction_Force | None = Field(default=None)
    scaling: DimensionalFunction_Dimensionless | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
