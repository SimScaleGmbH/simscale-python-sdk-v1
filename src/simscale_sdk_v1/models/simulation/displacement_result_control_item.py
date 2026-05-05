from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.global_displacement_type import GlobalDisplacementType


class DisplacementResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISPLACEMENT",
        description="Schema name: DisplacementResultControlItem",
    )
    name: str | None = Field(default=None)
    displacement_type: GlobalDisplacementType | None = Field(
        validation_alias="displacementType", serialization_alias="displacementType", default=None
    )
