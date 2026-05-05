from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OpaqueMaterial(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OPAQUE_MATERIAL",
        description="Schema name: OpaqueMaterial",
    )
    emissivity: float | None = Field(default=0.9)
