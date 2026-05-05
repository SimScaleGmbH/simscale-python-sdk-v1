from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OutsideRegionRefinementWithLevels(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTSIDE",
        description="Schema name: OutsideRegionRefinementWithLevels",
    )
    level: int | None = Field(default=1)
