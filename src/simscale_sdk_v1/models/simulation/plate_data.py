from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__plate_data_hole_shape import OneOf_PlateDataHoleShape


class PlateData(SimScaleModel):
    free_area_ratio: float | None = Field(
        validation_alias="freeAreaRatio",
        serialization_alias="freeAreaRatio",
        default=0.5,
        description="Free area ratio is the ratio of open area of the perforated plate to its total area.",
    )
    hole_shape: OneOf_PlateDataHoleShape | None = Field(
        validation_alias="holeShape", serialization_alias="holeShape", default=None
    )
