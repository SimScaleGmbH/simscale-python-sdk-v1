from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.normalized_displacement_type import NormalizedDisplacementType


class NormalizedDisplacementResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NORMALIZED_DISPLACEMENT",
        description="Schema name: NormalizedDisplacementResultControlItem",
    )
    name: str | None = Field(default=None)
    displacement_type: NormalizedDisplacementType | None = Field(
        validation_alias="displacementType", serialization_alias="displacementType", default=None
    )
