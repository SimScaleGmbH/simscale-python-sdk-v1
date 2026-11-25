from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function_with_lcs__angle import (
    DimensionalPartialVectorFunctionWithLCS_Angle,
)
from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function_with_lcs__length import (
    DimensionalPartialVectorFunctionWithLCS_Length,
)
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
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the Displacement and Rotation components are expressed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Note: the coordinates of the External point are still expresed in the Global coordinate system.",
    )
    displacement_components: DimensionalPartialVectorFunctionWithLCS_Length | None = Field(
        validation_alias="displacementComponents", serialization_alias="displacementComponents", default=None
    )
    rotation_components: DimensionalPartialVectorFunctionWithLCS_Angle | None = Field(
        validation_alias="rotationComponents", serialization_alias="rotationComponents", default=None
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
    point_primitive_uuid: str | None = Field(
        validation_alias="pointPrimitiveUuid",
        serialization_alias="pointPrimitiveUuid",
        default=None,
        description="Choose how the remote point which is imposing the displacement is defined. This will be the point along which the translation and rotation will take place.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
