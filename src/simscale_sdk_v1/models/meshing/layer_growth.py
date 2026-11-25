from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class LayerGrowth(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LAYER_GROWTH",
        description="Schema name: LayerGrowth",
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
