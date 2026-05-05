from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.region_interface import RegionInterface


class FluidInterface(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLUID_INTERFACE",
        description="Schema name: FluidInterface",
    )
    connections: list[RegionInterface] | None = Field(default=None)
