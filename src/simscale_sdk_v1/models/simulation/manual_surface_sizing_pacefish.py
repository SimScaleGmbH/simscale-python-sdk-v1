from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.additional_directional_cells import AdditionalDirectionalCells
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class ManualSurfaceSizingPacefish(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_SURFACE_PACEFISH",
        description="Schema name: ManualSurfaceSizingPacefish",
    )
    target_resolution: Dimensional_Length | None = Field(
        validation_alias="targetResolution", serialization_alias="targetResolution", default=None
    )
    buffer_cells_no_extrude: int | None = Field(
        validation_alias="bufferCellsNoExtrude",
        serialization_alias="bufferCellsNoExtrude",
        default=4,
        description="Specify the minimum number of buffer cells between regions of different refinements.",
    )
    additional_directional_cells: AdditionalDirectionalCells | None = Field(
        validation_alias="additionalDirectionalCells", serialization_alias="additionalDirectionalCells", default=None
    )
