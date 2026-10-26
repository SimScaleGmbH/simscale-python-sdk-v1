from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class Gap(SimScaleModel):
    region_a: str = Field(
        validation_alias="regionA", serialization_alias="regionA", description="Solid region on one side of the gap."
    )
    faces_a: list[str] = Field(
        validation_alias="facesA", serialization_alias="facesA", description="Faces on one side of the gap."
    )
    region_b: str = Field(
        validation_alias="regionB",
        serialization_alias="regionB",
        description="Solid region on another side of the gap.",
    )
    faces_b: list[str] = Field(
        validation_alias="facesB", serialization_alias="facesB", description="Faces on another side of the gap."
    )
    size: Length
