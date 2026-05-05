from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class InletOutletTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_OUTLET",
        description="Schema name: InletOutletTBC",
    )
    value: Dimensional_Temperature | None = Field(default=None)
