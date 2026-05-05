from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed


class PressureCoefficientResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE_COEFFICIENT",
        description="Schema name: PressureCoefficientResultType",
    )
    free_stream_pressure: Dimensional_Pressure | None = Field(
        validation_alias="freeStreamPressure", serialization_alias="freeStreamPressure", default=None
    )
    free_stream_velocity: DimensionalVector_Speed | None = Field(
        validation_alias="freeStreamVelocity", serialization_alias="freeStreamVelocity", default=None
    )
