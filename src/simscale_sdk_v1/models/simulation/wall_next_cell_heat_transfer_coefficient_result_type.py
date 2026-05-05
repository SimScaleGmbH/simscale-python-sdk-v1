from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WallNextCellHeatTransferCoefficientResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_NEXT_CELL_HEAT_TRANSFER_COEFFICIENT",
        description="Schema name: WallNextCellHeatTransferCoefficientResultType",
    )
