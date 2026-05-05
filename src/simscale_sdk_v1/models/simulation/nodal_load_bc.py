from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector_function__force import DimensionalVectorFunction_Force
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class NodalLoadBC(SimScaleModel):
    """This is a force boundary condition representing an equal point force on each node of the assignment. The total force applied on the assignment is calculated as the user defined forces times the number of nodes in the assignment.Important remarks: Currently, it only works on uploaded meshesAs the total load is depending on the number of nodes, and thus the mesh fineness, it is recommended only for loads on single nodes.In most cases point loads are unphysical and distributed loads should be used instead."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NODAL_LOAD",
        description="This is a force boundary condition representing an equal point force on each node of the assignment. The total force applied on the assignment is calculated as the user defined forces times the number of nodes in the assignment.Important remarks: Currently, it only works on uploaded meshesAs the total load is depending on the number of nodes, and thus the mesh fineness, it is recommended only for loads on single nodes.In most cases point loads are unphysical and distributed loads should be used instead.  Schema name: NodalLoadBC",
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
