from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__absorptivity import Dimensional_Absorptivity
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_transmittance import (
    DimensionalFunction_ThermalTransmittance,
)


class HeatTransferCoefficients(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HEAT_TRANSFER_COEFFICIENTS",
        description="Schema name: HeatTransferCoefficients",
    )
    ref_temperature: DimensionalFunction_Temperature | None = Field(
        validation_alias="refTemperature", serialization_alias="refTemperature", default=None
    )
    heat_transfer_coefficient: DimensionalFunction_ThermalTransmittance | None = Field(
        validation_alias="heatTransferCoefficient", serialization_alias="heatTransferCoefficient", default=None
    )
    surface_area_density: Dimensional_Absorptivity | None = Field(
        validation_alias="surfaceAreaDensity", serialization_alias="surfaceAreaDensity", default=None
    )
    heat_distribution: Literal["LOCAL", "AVERAGE"] | None = Field(
        validation_alias="heatDistribution",
        serialization_alias="heatDistribution",
        default="LOCAL",
        description="Sampling method for the field temperature (T) in T - Tref. This indicates whether the temperature (T) is averaged on the complete heat exchanger or sampled at each position.",
    )
