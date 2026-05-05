from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeConvergenceDisplacements(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE",
        description="Schema name: RelativeConvergenceDisplacements",
    )
    relative_displacement_tolerance: float | None = Field(
        validation_alias="relativeDisplacementTolerance",
        serialization_alias="relativeDisplacementTolerance",
        default=0.1,
        description="The ratio of the maximum displacement change in the current iteration to the maximum displacement in the current increment. It ensures the geometry has stopped changing significantly before finishing the step.",
    )
    relative_rotation_tolerance: float | None = Field(
        validation_alias="relativeRotationTolerance", serialization_alias="relativeRotationTolerance", default=0.0
    )
