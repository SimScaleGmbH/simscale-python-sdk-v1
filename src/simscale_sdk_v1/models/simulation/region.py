from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Region(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="REGION", description="Schema name: Region"
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
