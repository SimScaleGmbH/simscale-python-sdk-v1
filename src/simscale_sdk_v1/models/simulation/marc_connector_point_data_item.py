from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_connector_point_data_item_results import (
    OneOf_MarcConnectorPointDataItemResults,
)


class MarcConnectorPointDataItem(SimScaleModel):
    name: str | None = Field(default=None)
    results: OneOf_MarcConnectorPointDataItemResults | None = Field(default=None)
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
