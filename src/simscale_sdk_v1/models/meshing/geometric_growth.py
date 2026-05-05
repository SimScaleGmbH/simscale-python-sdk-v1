from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class GeometricGrowth(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GEOMETRIC_GROWTH",
        description="Schema name: GeometricGrowth",
    )
    number_of_layers: int | None = Field(
        validation_alias="numberOfLayers",
        serialization_alias="numberOfLayers",
        default=3,
        description="The Number of layers defines how many prismatic boundary layers should be created. 3 is default.",
    )
    total_absolute_thickness: Dimensional_Length | None = Field(
        validation_alias="totalAbsoluteThickness", serialization_alias="totalAbsoluteThickness", default=None
    )
    first_layer_size: Dimensional_Length | None = Field(
        validation_alias="firstLayerSize", serialization_alias="firstLayerSize", default=None
    )
