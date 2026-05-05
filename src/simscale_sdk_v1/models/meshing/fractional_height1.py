from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class FractionalHeight1(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRACTIONAL_HEIGHT_1",
        description="Schema name: FractionalHeight1",
    )
    number_of_layers: int | None = Field(
        validation_alias="numberOfLayers",
        serialization_alias="numberOfLayers",
        default=3,
        description="The Number of layers defines how many prismatic boundary layers should be created. 3 is default.",
    )
    total_relative_thickness: float | None = Field(
        validation_alias="totalRelativeThickness",
        serialization_alias="totalRelativeThickness",
        default=0.4,
        description="It defines the thickness of all prismatic boundary layers combined in relation to the local element size.Example 3-layer thickness of 40% (0.4) of the local mesh size.",
    )
    first_layer_size: Dimensional_Length | None = Field(
        validation_alias="firstLayerSize", serialization_alias="firstLayerSize", default=None
    )
