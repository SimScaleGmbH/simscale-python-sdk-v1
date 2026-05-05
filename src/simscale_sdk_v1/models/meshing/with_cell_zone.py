from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WithCellZone(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WITH_CELL_ZONE_V11",
        description="Schema name: WithCellZone",
    )
    name: str | None = Field(default="Zone")
