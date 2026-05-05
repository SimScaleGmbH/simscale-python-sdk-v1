from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_function__dimensionless import DimensionalFunction_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.dimensional_vector_function__force import DimensionalVectorFunction_Force
from simscale_sdk_v1.models.simulation.dimensional_vector_function__torque import DimensionalVectorFunction_Torque
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
    force: DimensionalVectorFunction_Force | None = Field(default=None)
    moment: DimensionalVectorFunction_Torque | None = Field(default=None)
    scaling: DimensionalFunction_Dimensionless | None = Field(default=None)
    phase_angle: Dimensional_Angle | None = Field(
        validation_alias="phaseAngle", serialization_alias="phaseAngle", default=None
    )
    remote_point: DimensionalVector_Length | None = Field(
        validation_alias="remotePoint", serialization_alias="remotePoint", default=None
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
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
