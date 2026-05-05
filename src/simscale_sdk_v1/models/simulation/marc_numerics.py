from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.marc_linear_solver_settings import MarcLinearSolverSettings
from simscale_sdk_v1.models.simulation.marc_nonlinear_solver_settings import MarcNonlinearSolverSettings


class MarcNumerics(SimScaleModel):
    linear_solver_settings: MarcLinearSolverSettings | None = Field(
        validation_alias="linearSolverSettings", serialization_alias="linearSolverSettings", default=None
    )
    nonlinear_solver_settings: MarcNonlinearSolverSettings | None = Field(
        validation_alias="nonlinearSolverSettings", serialization_alias="nonlinearSolverSettings", default=None
    )
