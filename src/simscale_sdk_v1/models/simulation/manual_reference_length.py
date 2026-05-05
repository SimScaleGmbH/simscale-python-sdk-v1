from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class ManualReferenceLength(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_REFERENCE_LENGTH",
        description="Schema name: ManualReferenceLength",
    )
    value: Dimensional_Length | None = Field(default=None)
