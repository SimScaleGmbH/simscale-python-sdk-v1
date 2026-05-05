from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class HeatFluxResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HEAT_FLUX",
        description="Schema name: HeatFluxResultControlItem",
    )
    name: str | None = Field(default=None)
    heat_flux_type: Literal["FIELD"] | None = Field(
        validation_alias="heatFluxType", serialization_alias="heatFluxType", default="FIELD"
    )
