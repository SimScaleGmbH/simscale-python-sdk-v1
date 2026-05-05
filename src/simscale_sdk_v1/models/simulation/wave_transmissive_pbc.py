from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class WaveTransmissivePBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WAVE_TRANSMISSIVE",
        description="Schema name: WaveTransmissivePBC",
    )
    specific_heat_ratio: float | None = Field(
        validation_alias="specificHeatRatio", serialization_alias="specificHeatRatio", default=1.4
    )
    relax_boundary: bool | None = Field(
        validation_alias="relaxBoundary", serialization_alias="relaxBoundary", default=False
    )
    far_field_value: Dimensional_Pressure | None = Field(
        validation_alias="farFieldValue", serialization_alias="farFieldValue", default=None
    )
    relaxation_length_scale: Dimensional_Length | None = Field(
        validation_alias="relaxationLengthScale", serialization_alias="relaxationLengthScale", default=None
    )
