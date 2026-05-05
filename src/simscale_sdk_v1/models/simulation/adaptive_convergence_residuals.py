from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__force import Dimensional_Force
from simscale_sdk_v1.models.simulation.dimensional__torque import Dimensional_Torque


class AdaptiveConvergenceResiduals(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ADAPTIVE",
        description="Schema name: AdaptiveConvergenceResiduals",
    )
    relative_force_tolerance: float | None = Field(
        validation_alias="relativeForceTolerance",
        serialization_alias="relativeForceTolerance",
        default=0.05,
        description="The ratio of the maximum residual force to the maximum reaction force (or applied load). A typical value is 5 &times; 10-2 (5%) or 10-2, ensuring that the error in force balance is negligible.",
    )
    max_residual_force: Dimensional_Force | None = Field(
        validation_alias="maxResidualForce", serialization_alias="maxResidualForce", default=None
    )
    relative_moment_tolerance: float | None = Field(
        validation_alias="relativeMomentTolerance", serialization_alias="relativeMomentTolerance", default=0.0
    )
    max_residual_moment: Dimensional_Torque | None = Field(
        validation_alias="maxResidualMoment", serialization_alias="maxResidualMoment", default=None
    )
