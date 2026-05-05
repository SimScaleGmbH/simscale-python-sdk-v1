from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TrueChangeJacobianMatrix(SimScaleModel):
    """Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TRUE",
        description="Choose if the Jacobian matrix should automatically change from tangent stiffnes matrix to elastic matrix if the time increment is falling below a given threshold. On the assumption that below a given time increment value the nonlinearities are not evolving within the time step one can strongly save computation time by switching to the elastic matrix.  Schema name: TrueChangeJacobianMatrix",
    )
    threshold_time_step_value: float | None = Field(
        validation_alias="thresholdTimeStepValue",
        serialization_alias="thresholdTimeStepValue",
        default=1e-06,
        description="Set the threshold value of the Jacobian matrix changing. If the time increment is lower than this value the elastic matrix is used.",
    )
    matrix_reactualization_iteration: int | None = Field(
        validation_alias="matrixReactualizationIteration",
        serialization_alias="matrixReactualizationIteration",
        default=0,
        description="Set how often the elastic stiffness matrix should be recomputed. If this parameter is set to 10, the elastic matrix is recomputed every 10th iteration within a given time step. If it is set to 0, the elastic stiffness matrix is not updated within any time step.",
    )
    max_newton_iterations: int | None = Field(
        validation_alias="maxNewtonIterations",
        serialization_alias="maxNewtonIterations",
        default=35,
        description="Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.",
    )
