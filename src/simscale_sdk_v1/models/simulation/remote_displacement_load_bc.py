from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__angle import (
    DimensionalPartialVectorFunction_Angle,
)
from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__length import (
    DimensionalPartialVectorFunction_Length,
)
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RemoteDisplacementLoadBC(SimScaleModel):
    """This boundary condition restrains the displacement of a face or edge relative to a specified remote point. Therefore the assignment is connected to the remote point with RBE3 (deformable) or MPC (undeformable) conditions and the defined constraints are applied to the remote point.Important remarks: As the assignments are connected to the remote point, additional constraints on these nodes may lead to overconstrained systems.If the number of nodes of the assigment is large (>1000), it is recommended to use the MUMPS or PETSC solver.This boundary condition is only valid for small rotations. For large rotations, please use Rotating motion boundary conditions.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REMOTE_DISPLACEMENT_LOAD",
        description="This boundary condition restrains the displacement of a face or edge relative to a specified remote point. Therefore the assignment is connected to the remote point with RBE3 (deformable) or MPC (undeformable) conditions and the defined constraints are applied to the remote point.Important remarks: As the assignments are connected to the remote point, additional constraints on these nodes may lead to overconstrained systems.If the number of nodes of the assigment is large (>1000), it is recommended to use the MUMPS or PETSC solver.This boundary condition is only valid for small rotations. For large rotations, please use Rotating motion boundary conditions.Learn more.   Schema name: RemoteDisplacementLoadBC",
    )
    name: str | None = Field(default=None)
    displacement: DimensionalPartialVectorFunction_Length | None = Field(default=None)
    rotation: DimensionalPartialVectorFunction_Angle | None = Field(default=None)
    external_point: DimensionalVector_Length | None = Field(
        validation_alias="externalPoint", serialization_alias="externalPoint", default=None
    )
    deformation_behavior: Literal["DEFORMABLE", "UNDEFORMABLE"] | None = Field(
        validation_alias="deformationBehavior",
        serialization_alias="deformationBehavior",
        default="DEFORMABLE",
        description="Choose the deformation behavior of the assigned entity. If deformable is selected, the entity is allowed to deform, selecting undeformable leads to a rigid entity.",
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
