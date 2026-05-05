from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class FirstLayerGrowth(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIRST_LAYER_GROWTH",
        description="Schema name: FirstLayerGrowth",
    )
    number_of_layers: int | None = Field(
        validation_alias="numberOfLayers",
        serialization_alias="numberOfLayers",
        default=3,
        description="The Number of layers defines how many prismatic boundary layers should be created. 3 is default.",
    )
    growth_rate: float | None = Field(
        validation_alias="growthRate",
        serialization_alias="growthRate",
        default=1.3,
        description="The Growth rate defines the thickness ratio between adjacent boundary layer cells. It needs to be always greater than 1 such that the layer thickness increases towards the interior of the mesh. For the same number of layers and overall thickness the larger the growth rate is inversely proportional to the first cell thickness. Example of each cell being 1.5 times thicker than its adjacent.",
    )
    first_layer_size: Dimensional_Length | None = Field(
        validation_alias="firstLayerSize", serialization_alias="firstLayerSize", default=None
    )
