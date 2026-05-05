from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class AdaptiveConvergenceDisplacements(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ADAPTIVE",
        description="Schema name: AdaptiveConvergenceDisplacements",
    )
    relative_displacement_tolerance: float | None = Field(
        validation_alias="relativeDisplacementTolerance",
        serialization_alias="relativeDisplacementTolerance",
        default=0.1,
        description="The ratio of the maximum displacement change in the current iteration to the maximum displacement in the current increment. It ensures the geometry has stopped changing significantly before finishing the step.",
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
