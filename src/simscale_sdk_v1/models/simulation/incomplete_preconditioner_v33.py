from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class IncompletePreconditionerV33(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INCOMPLETE_LDLT_V33",
        description="Schema name: IncompletePreconditionerV33",
    )
    matrix_completeness: int | None = Field(
        validation_alias="matrixCompleteness",
        serialization_alias="matrixCompleteness",
        default=0,
        description="Set the level of completeness for the incomplete Cholesky decomposition. The larger this value is, the better the preconditioning Matrix P approximates K-1, but also the memory usage and computation time increase. If the solution does not converge or uses a lot of iterations it could help to increase this parameter.",
    )
    preconditioner_matrix_growth: float | None = Field(
        validation_alias="preconditionerMatrixGrowth",
        serialization_alias="preconditionerMatrixGrowth",
        default=1,
        description="Set the growth rate of the filling for the incomplete decomposition matrix. If this parameter is set to 1.0 PETSc estimates the matrix storage size from the first level of completeness. If this estimate is too low, PETSC increases the allocated memory on the fly, but this is more expensive.",
    )
