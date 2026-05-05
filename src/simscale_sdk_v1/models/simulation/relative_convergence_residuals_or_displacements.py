from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeConvergenceResidualsOrDisplacements(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE",
        description="Schema name: RelativeConvergenceResidualsOrDisplacements",
    )
    relative_force_tolerance: float | None = Field(
        validation_alias="relativeForceTolerance", serialization_alias="relativeForceTolerance", default=0.05
    )
    relative_moment_tolerance: float | None = Field(
        validation_alias="relativeMomentTolerance", serialization_alias="relativeMomentTolerance", default=0.0
    )
    relative_displacement_tolerance: float | None = Field(
        validation_alias="relativeDisplacementTolerance",
        serialization_alias="relativeDisplacementTolerance",
        default=0.1,
    )
    relative_rotation_tolerance: float | None = Field(
        validation_alias="relativeRotationTolerance", serialization_alias="relativeRotationTolerance", default=0.0
    )
