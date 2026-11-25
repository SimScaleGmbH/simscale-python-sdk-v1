from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector_function_with_lcs__force import (
    DimensionalVectorFunctionWithLCS_Force,
)
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
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the vector components are expressed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Cylindrical — Vector components are defined as radial (ur), tangential (uΦ), and axial (uz).",
    )
    force_components: DimensionalVectorFunctionWithLCS_Force | None = Field(
        validation_alias="forceComponents", serialization_alias="forceComponents", default=None
    )
    scaling: DimensionalFunction_Dimensionless | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
