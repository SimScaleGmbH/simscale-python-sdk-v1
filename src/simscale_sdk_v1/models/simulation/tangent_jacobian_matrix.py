from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__tangent_jacobian_matrix_change_jacobian_matrix import (
    OneOf_TangentJacobianMatrixChangeJacobianMatrix,
)


class TangentJacobianMatrix(SimScaleModel):
    """Select which stiffnes matrix should be used for computing the Jacobian of the Newton method. Choosing the tangent stiffnes matrix via tangent matrix allows a full Newton approach whereas the selection of the elastic matrix results in a quasi-Newton approach."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TANGENT",
        description="Select which stiffnes matrix should be used for computing the Jacobian of the Newton method. Choosing the tangent stiffnes matrix via tangent matrix allows a full Newton approach whereas the selection of the elastic matrix results in a quasi-Newton approach.  Schema name: TangentJacobianMatrix",
    )
    max_newton_iteration: int | None = Field(
        validation_alias="maxNewtonIteration",
        serialization_alias="maxNewtonIteration",
        default=35,
        description="Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.",
    )
    reactualization_iteration: int | None = Field(
        validation_alias="reactualizationIteration",
        serialization_alias="reactualizationIteration",
        default=None,
        description="Select how often the Jacobian matrix should be recomputed. If this parameter is set to 10, the Jacobian matrix is recomputed every 10th iteration within a given time step. If it is set to 0, the Jacobian matrix is not updated within any time step.",
    )
    reactualization_increment: int | None = Field(
        validation_alias="reactualizationIncrement",
        serialization_alias="reactualizationIncrement",
        default=1,
        description="Select how often the Jacobian matrix should be recomputed. If this parameter is set to 10, the Jacobian matrix is recomputed every 10th time step. If it is set to 0, the Jacobian matrix is never updated.",
    )
    change_jacobian_matrix: OneOf_TangentJacobianMatrixChangeJacobianMatrix | None = Field(
        validation_alias="changeJacobianMatrix", serialization_alias="changeJacobianMatrix", default=None
    )
