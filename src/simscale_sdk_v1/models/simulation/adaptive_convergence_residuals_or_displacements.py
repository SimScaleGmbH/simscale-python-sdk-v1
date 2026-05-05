from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__force import Dimensional_Force
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__torque import Dimensional_Torque


class AdaptiveConvergenceResidualsOrDisplacements(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ADAPTIVE",
        description="Schema name: AdaptiveConvergenceResidualsOrDisplacements",
    )
    relative_force_tolerance: float | None = Field(
        validation_alias="relativeForceTolerance", serialization_alias="relativeForceTolerance", default=0.05
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
    relative_displacement_tolerance: float | None = Field(
        validation_alias="relativeDisplacementTolerance",
        serialization_alias="relativeDisplacementTolerance",
        default=0.1,
    )
    max_displacement_increment: Dimensional_Length | None = Field(
        validation_alias="maxDisplacementIncrement", serialization_alias="maxDisplacementIncrement", default=None
    )
    relative_rotation_tolerance: float | None = Field(
        validation_alias="relativeRotationTolerance", serialization_alias="relativeRotationTolerance", default=0.0
    )
    max_rotation_increment: Dimensional_Angle | None = Field(
        validation_alias="maxRotationIncrement", serialization_alias="maxRotationIncrement", default=None
    )
