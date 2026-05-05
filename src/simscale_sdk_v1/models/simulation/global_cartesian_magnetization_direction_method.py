from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless


class GlobalCartesianMagnetizationDirectionMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GLOBAL_CARTESIAN",
        description="Schema name: GlobalCartesianMagnetizationDirectionMethod",
    )
    magnetization_direction: DimensionalVector_Dimensionless | None = Field(
        validation_alias="magnetizationDirection", serialization_alias="magnetizationDirection", default=None
    )
