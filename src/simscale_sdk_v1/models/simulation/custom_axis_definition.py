from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__dimensionless import DimensionalVector_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class CustomAxisDefinition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomAxisDefinition",
    )
    axis_origin: DimensionalVector_Length | None = Field(
        validation_alias="axisOrigin", serialization_alias="axisOrigin", default=None
    )
    axis_direction: DimensionalVector_Dimensionless | None = Field(
        validation_alias="axisDirection", serialization_alias="axisDirection", default=None
    )
