from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class AbsoluteToAllCadSurfacesSettings(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE_TO_ALL_CAD_SURFACES",
        description="Schema name: AbsoluteToAllCadSurfacesSettings",
    )
    minimum_cell_size: Dimensional_Length | None = Field(
        validation_alias="minimumCellSize", serialization_alias="minimumCellSize", default=None
    )
    maximum_cell_size: Dimensional_Length | None = Field(
        validation_alias="maximumCellSize", serialization_alias="maximumCellSize", default=None
    )
    cell_size_on_surfaces: Dimensional_Length | None = Field(
        validation_alias="cellSizeOnSurfaces", serialization_alias="cellSizeOnSurfaces", default=None
    )
    enable_growth_rate: bool | None = Field(
        validation_alias="enableGrowthRate",
        serialization_alias="enableGrowthRate",
        default=False,
        description="Specify growth rate: Define the cell size growth rate between interior cells and surface cells.",
    )
    growth_rate: int | None = Field(
        validation_alias="growthRate",
        serialization_alias="growthRate",
        default=2,
        description="The Growth rate defines the cell size ratio between interior cell size and surface cell size. It needs to be a whole number always greater than 1 and smaller or equal to 8, such that the cell size increases towards the interior of the mesh.",
    )
