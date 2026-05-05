from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GeometryPrimitiveResponse(SimScaleModel):
    geometry_primitive_id: str = Field(
        validation_alias="geometryPrimitiveId",
        serialization_alias="geometryPrimitiveId",
        description="The ID of the created geometry primitive.",
    )
