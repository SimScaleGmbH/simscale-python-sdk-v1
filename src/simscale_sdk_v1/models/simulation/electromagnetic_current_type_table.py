from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__electric_current import DimensionalFunction_ElectricCurrent


class ElectromagneticCurrentTypeTable(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CURRENT_TYPE_TABLE",
        description="Schema name: ElectromagneticCurrentTypeTable",
    )
    values: DimensionalFunction_ElectricCurrent | None = Field(default=None)
