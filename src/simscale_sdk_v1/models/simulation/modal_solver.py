from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.calculate_frequency import CalculateFrequency
from simscale_sdk_v1.models.simulation.eigen_mode_verification import EigenModeVerification
from simscale_sdk_v1.models.simulation.one_of__modal_solver_eigen_solver import OneOf_ModalSolverEigenSolver
from simscale_sdk_v1.models.simulation.one_of__modal_solver_solver import OneOf_ModalSolverSolver
from simscale_sdk_v1.models.simulation.solver_model import SolverModel


class ModalSolver(SimScaleModel):
    solver: OneOf_ModalSolverSolver | None = Field(default=None)
    solver_model: SolverModel | None = Field(
        validation_alias="solverModel", serialization_alias="solverModel", default=None
    )
    eigen_solver: OneOf_ModalSolverEigenSolver | None = Field(
        validation_alias="eigenSolver", serialization_alias="eigenSolver", default=None
    )
    calculate_frequency: CalculateFrequency | None = Field(
        validation_alias="calculateFrequency", serialization_alias="calculateFrequency", default=None
    )
    eigen_mode: EigenModeVerification | None = Field(
        validation_alias="eigenMode", serialization_alias="eigenMode", default=None
    )
    enhanced_accuracy: bool | None = Field(
        validation_alias="enhancedAccuracy",
        serialization_alias="enhancedAccuracy",
        default=False,
        description="Further increase the accuracy of the results by running two simulations. The results of the first one will be used as input for the second one to fine-tune the setup.",
    )
