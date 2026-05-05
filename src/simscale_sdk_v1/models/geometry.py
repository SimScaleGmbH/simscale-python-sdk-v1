from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Geometry(SimScaleModel):
    geometry_id: str | None = Field(validation_alias="geometryId", serialization_alias="geometryId", default=None)
    name: str | None = Field(default=None, description="The name of the geometry.")
    created_at: datetime | None = Field(
        validation_alias="createdAt",
        serialization_alias="createdAt",
        default=None,
        description="The time when the geometry was imported.",
    )
    format: str | None = Field(default=None, description="The geometry format.")
