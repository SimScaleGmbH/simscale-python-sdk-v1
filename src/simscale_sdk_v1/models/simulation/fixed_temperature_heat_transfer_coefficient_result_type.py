from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class FixedTemperatureHeatTransferCoefficientResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REFERENCE_TEMPERATURE_HEAT_TRANSFER_COEFFICIENT",
        description="Schema name: FixedTemperatureHeatTransferCoefficientResultType",
    )
    reference_heat_transfer_temperature: Dimensional_Temperature | None = Field(
        validation_alias="referenceHeatTransferTemperature",
        serialization_alias="referenceHeatTransferTemperature",
        default=None,
    )
