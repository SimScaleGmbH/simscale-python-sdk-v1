from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FluidOnlyHeatTransfer(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLUID_ONLY_HEAT_TRANSFER",
        description="Schema name: FluidOnlyHeatTransfer",
    )
