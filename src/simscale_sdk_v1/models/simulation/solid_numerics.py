from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.calculate_frequency import CalculateFrequency
from simscale_sdk_v1.models.simulation.eigen_mode_verification import EigenModeVerification
from simscale_sdk_v1.models.simulation.harmonic_response import HarmonicResponse
from simscale_sdk_v1.models.simulation.modal_solver import ModalSolver
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_eigen_solver import OneOf_SolidNumericsEigenSolver
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_line_search import (
    OneOf_SolidNumericsMechanicalLineSearch,
)
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_resolution_type import (
    OneOf_SolidNumericsMechanicalResolutionType,
)
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_mechanical_time_integration_type import (
    OneOf_SolidNumericsMechanicalTimeIntegrationType,
)
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_solver import OneOf_SolidNumericsSolver
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_thermal_line_search import (
    OneOf_SolidNumericsThermalLineSearch,
)
from simscale_sdk_v1.models.simulation.one_of__solid_numerics_thermal_resolution_type import (
    OneOf_SolidNumericsThermalResolutionType,
)
from simscale_sdk_v1.models.simulation.solver_model import SolverModel
from simscale_sdk_v1.models.simulation.theta_method_time_integration_type import ThetaMethodTimeIntegrationType


class SolidNumerics(SimScaleModel):
    harmonic_solution_method: Literal["MODAL_BASED", "DIRECT"] | None = Field(
        validation_alias="harmonicSolutionMethod",
        serialization_alias="harmonicSolutionMethod",
        default="DIRECT",
        description="Select the basis for the computation of the harmonic analysis.",
    )
    solver: OneOf_SolidNumericsSolver | None = Field(default=None)
    solve_model: SolverModel | None = Field(
        validation_alias="solveModel", serialization_alias="solveModel", default=None
    )
    eigen_solver: OneOf_SolidNumericsEigenSolver | None = Field(
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
    modal_base: ModalSolver | None = Field(validation_alias="modalBase", serialization_alias="modalBase", default=None)
    harmonic_response: HarmonicResponse | None = Field(
        validation_alias="harmonicResponse", serialization_alias="harmonicResponse", default=None
    )
    mechanical_time_integration_type: OneOf_SolidNumericsMechanicalTimeIntegrationType | None = Field(
        validation_alias="mechanicalTimeIntegrationType",
        serialization_alias="mechanicalTimeIntegrationType",
        default=None,
    )
    mechanical_resolution_type: OneOf_SolidNumericsMechanicalResolutionType | None = Field(
        validation_alias="mechanicalResolutionType", serialization_alias="mechanicalResolutionType", default=None
    )
    mechanical_line_search: OneOf_SolidNumericsMechanicalLineSearch | None = Field(
        validation_alias="mechanicalLineSearch", serialization_alias="mechanicalLineSearch", default=None
    )
    thermal_time_integration_type: ThetaMethodTimeIntegrationType | None = Field(
        validation_alias="thermalTimeIntegrationType", serialization_alias="thermalTimeIntegrationType", default=None
    )
    thermal_resolution_type: OneOf_SolidNumericsThermalResolutionType | None = Field(
        validation_alias="thermalResolutionType", serialization_alias="thermalResolutionType", default=None
    )
    thermal_line_search: OneOf_SolidNumericsThermalLineSearch | None = Field(
        validation_alias="thermalLineSearch", serialization_alias="thermalLineSearch", default=None
    )
    remote_point_stiffness_multiplier: float | None = Field(
        validation_alias="remotePointStiffnessMultiplier",
        serialization_alias="remotePointStiffnessMultiplier",
        default=0,
    )
