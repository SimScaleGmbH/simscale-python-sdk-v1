from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__stiffness import Dimensional_Stiffness


class FlexibleAxialTranslation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLEXIBLE",
        description="Schema name: FlexibleAxialTranslation",
    )
    axial_stiffness: Dimensional_Stiffness | None = Field(
        validation_alias="axialStiffness", serialization_alias="axialStiffness", default=None
    )
