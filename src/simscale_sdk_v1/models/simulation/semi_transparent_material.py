from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SemiTransparentMaterial(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SEMI_TRANSPARENT_MATERIAL",
        description="Schema name: SemiTransparentMaterial",
    )
    emissivity: float | None = Field(default=0.0)
    transmissivity: float | None = Field(default=0)
