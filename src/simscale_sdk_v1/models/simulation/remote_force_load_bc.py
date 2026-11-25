from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector_function_with_lcs__force import (
    DimensionalVectorFunctionWithLCS_Force,
)
from simscale_sdk_v1.models.simulation.dimensional_vector_function_with_lcs__torque import (
    DimensionalVectorFunctionWithLCS_Torque,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RemoteForceLoadBC(SimScaleModel):
    """This is a remote force boundary condition where the load is applied on the assignment via a remote point. Therefore the assignment is connected to the remote point with RBE3 (deformable) or MPC (undeformable) conditions and the defined force is applied to the remote point.Important remarks: The total force will be distributed on the selection.As the assignments are connected to the remote point, additional constraints on these nodes may lead to overconstrained systems.If the number of nodes of the assignment is large (>1000), it is recommended to use the MUMPS or PETSC solver.This boundary condition is only valid for small rotations. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REMOTE_FORCE_LOAD",
        description="This is a remote force boundary condition where the load is applied on the assignment via a remote point. Therefore the assignment is connected to the remote point with RBE3 (deformable) or MPC (undeformable) conditions and the defined force is applied to the remote point.Important remarks: The total force will be distributed on the selection.As the assignments are connected to the remote point, additional constraints on these nodes may lead to overconstrained systems.If the number of nodes of the assignment is large (>1000), it is recommended to use the MUMPS or PETSC solver.This boundary condition is only valid for small rotations. Learn more.  Schema name: RemoteForceLoadBC",
    )
    name: str | None = Field(default=None)
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the Force and Moment components are expressed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Note: the coordinates of the External point are still expresed in the Global coordinate system.",
    )
    force_components: DimensionalVectorFunctionWithLCS_Force | None = Field(
        validation_alias="forceComponents", serialization_alias="forceComponents", default=None
    )
    moment_components: DimensionalVectorFunctionWithLCS_Torque | None = Field(
        validation_alias="momentComponents", serialization_alias="momentComponents", default=None
    )
    scaling: DimensionalFunction_Dimensionless | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    deformation_behavior: Literal["DEFORMABLE", "UNDEFORMABLE"] | None = Field(
        validation_alias="deformationBehavior",
        serialization_alias="deformationBehavior",
        default="DEFORMABLE",
        description="Choose the deformation behavior of the assigned entity. If deformable is selected, the entitiy is allowed to deform without applying additional stiffness, selecting undeformable leads to a rigid entity.",
    )
    enable_search_radius: bool | None = Field(
        validation_alias="enableSearchRadius", serialization_alias="enableSearchRadius", default=False
    )
    search_radius: Dimensional_Length | None = Field(
        validation_alias="searchRadius", serialization_alias="searchRadius", default=None
    )
    point_primitive_uuid: str | None = Field(
        validation_alias="pointPrimitiveUuid", serialization_alias="pointPrimitiveUuid", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
