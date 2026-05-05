from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class YPlusRASResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DIMENSIONLESS_WALL_DISTANCE_YPLUS",
        description="Schema name: YPlusRASResultType",
    )
