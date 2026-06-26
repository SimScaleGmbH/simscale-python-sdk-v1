from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeConvergenceResiduals(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE",
        description="Schema name: RelativeConvergenceResiduals",
    )
    relative_force_tolerance: float | None = Field(
        validation_alias="relativeForceTolerance",
        serialization_alias="relativeForceTolerance",
        default=0.05,
        description="The ratio of the maximum residual force to the maximum reaction force (or applied load). A typical value is 5 &times; 10-2 (5%) or 10-2, ensuring that the error in force balance is negligible.",
    )
    relative_moment_tolerance: float | None = Field(
        validation_alias="relativeMomentTolerance", serialization_alias="relativeMomentTolerance", default=0.0
    )
    relative_residual_auto_switch: bool | None = Field(
        validation_alias="relativeResidualAutoSwitch",
        serialization_alias="relativeResidualAutoSwitch",
        default=True,
        description="Auto switch method: Automatically toggles the convergence criteria between residual, displacement, or energy methods if the primary method becomes numerically unstable due to near-zero reactions or displacements. It is recommended for complex nonlinear assemblies to maintain progress without manually relaxing the tolerances.",
    )
