from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.marc_global_displacement_field_type import MarcGlobalDisplacementFieldType


class MarcDisplacementFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISPLACEMENT",
        description="Schema name: MarcDisplacementFieldSelection",
    )
    displacement_type: MarcGlobalDisplacementFieldType | None = Field(
        validation_alias="displacementType", serialization_alias="displacementType", default=None
    )
