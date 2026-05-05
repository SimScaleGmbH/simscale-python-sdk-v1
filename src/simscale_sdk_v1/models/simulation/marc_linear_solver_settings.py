from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_linear_solver_settings_linear_solver import (
    OneOf_MarcLinearSolverSettingsLinearSolver,
)


class MarcLinearSolverSettings(SimScaleModel):
    linear_solver: OneOf_MarcLinearSolverSettingsLinearSolver | None = Field(
        validation_alias="linearSolver", serialization_alias="linearSolver", default=None
    )
