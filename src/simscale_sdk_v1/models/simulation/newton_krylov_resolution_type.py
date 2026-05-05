from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__newton_krylov_resolution_type_convergence_criteria import (
    OneOf_NewtonKrylovResolutionTypeConvergenceCriteria,
)
from simscale_sdk_v1.models.simulation.one_of__newton_krylov_resolution_type_jacobian_matrix import (
    OneOf_NewtonKrylovResolutionTypeJacobianMatrix,
)


class NewtonKrylovResolutionType(SimScaleModel):
    """Choose how the nonlinearities are solved. Currently for direct solvers only the Newton-Raphson method is available via the selection Newton. For iterative solvers also an inexact version of the Newton-Raphson method is available via the selection Newton-Krylov."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NEWTON_KRYLOV",
        description="Choose how the nonlinearities are solved. Currently for direct solvers only the Newton-Raphson method is available via the selection Newton. For iterative solvers also an inexact version of the Newton-Raphson method is available via the selection Newton-Krylov.  Schema name: NewtonKrylovResolutionType",
    )
    convergence_criteria: OneOf_NewtonKrylovResolutionTypeConvergenceCriteria | None = Field(
        validation_alias="convergenceCriteria", serialization_alias="convergenceCriteria", default=None
    )
    prediction_matrix: Literal["TANGENT", "ELASTIC"] | None = Field(
        validation_alias="predictionMatrix",
        serialization_alias="predictionMatrix",
        default="TANGENT",
        description="Select which stiffnes matrix should be used in the prediction phase of the Newton method. A good choice leads to a good starting point for the first Newton iteration and thus a faster convergence.",
    )
    jacobian_matrix: OneOf_NewtonKrylovResolutionTypeJacobianMatrix | None = Field(
        validation_alias="jacobianMatrix", serialization_alias="jacobianMatrix", default=None
    )
