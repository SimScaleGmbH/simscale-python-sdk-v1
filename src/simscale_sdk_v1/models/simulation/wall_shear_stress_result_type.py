from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WallShearStressResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WALL_SHEAR_STRESS",
        description="Schema name: WallShearStressResultType",
    )
