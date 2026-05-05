from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FractionalHeight2(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRACTIONAL_HEIGHT_2",
        description="Schema name: FractionalHeight2",
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
    growth_rate: float | None = Field(
        validation_alias="growthRate",
        serialization_alias="growthRate",
        default=1.5,
        description="The Growth rate defines the thickness ratio between adjacent boundary layer cells. It needs to be always greater than 1 such that the layer thickness increases towards the interior of the mesh. For the same number of layers and overall thickness the larger the growth rate is inversely proportional to the first cell thickness. Example of each cell being 1.5 times thicker than its adjacent.",
    )
