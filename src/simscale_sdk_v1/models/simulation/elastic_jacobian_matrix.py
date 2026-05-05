from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ElasticJacobianMatrix(SimScaleModel):
    """Select which stiffnes matrix should be used for computing the Jacobian of the Newton method. Choosing the tangent stiffnes matrix via tangent matrix allows a full Newton approach whereas the selection of the elastic matrix results in a quasi-Newton approach."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELASTIC",
        description="Select which stiffnes matrix should be used for computing the Jacobian of the Newton method. Choosing the tangent stiffnes matrix via tangent matrix allows a full Newton approach whereas the selection of the elastic matrix results in a quasi-Newton approach.  Schema name: ElasticJacobianMatrix",
    )
    max_newton_iteration: int | None = Field(
        validation_alias="maxNewtonIteration",
        serialization_alias="maxNewtonIteration",
        default=35,
        description="Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.",
    )
