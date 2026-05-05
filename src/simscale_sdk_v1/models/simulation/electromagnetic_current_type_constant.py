from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__electric_current import Dimensional_ElectricCurrent


class ElectromagneticCurrentTypeConstant(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CURRENT_TYPE_CONSTANT",
        description="Schema name: ElectromagneticCurrentTypeConstant",
    )
    value: Dimensional_ElectricCurrent | None = Field(default=None)
