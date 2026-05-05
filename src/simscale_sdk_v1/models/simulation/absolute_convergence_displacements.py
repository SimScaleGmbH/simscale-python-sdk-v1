from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class AbsoluteConvergenceDisplacements(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE",
        description="Schema name: AbsoluteConvergenceDisplacements",
    )
    max_displacement_increment: Dimensional_Length | None = Field(
        validation_alias="maxDisplacementIncrement", serialization_alias="maxDisplacementIncrement", default=None
    )
    max_rotation_increment: Dimensional_Angle | None = Field(
        validation_alias="maxRotationIncrement", serialization_alias="maxRotationIncrement", default=None
    )
