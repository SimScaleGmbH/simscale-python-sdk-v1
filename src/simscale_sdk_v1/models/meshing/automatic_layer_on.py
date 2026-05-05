from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__automatic_layer_on_layer_type import OneOf_AutomaticLayerOnLayerType


class AutomaticLayerOn(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_LAYER_ON",
        description="Schema name: AutomaticLayerOn",
    )
    layer_type: OneOf_AutomaticLayerOnLayerType | None = Field(
        validation_alias="layerType", serialization_alias="layerType", default=None
    )
