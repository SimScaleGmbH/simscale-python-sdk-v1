from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class ShipDesignAnalysisSBM(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SHIP_DESIGN_ANALYSIS",
        description="Schema name: ShipDesignAnalysisSBM",
    )
    name: str | None = Field(default=None)
    center_of_gravity: DimensionalVector_Length | None = Field(
        validation_alias="centerOfGravity", serialization_alias="centerOfGravity", default=None
    )
    model_scale_ratio: float | None = Field(
        validation_alias="modelScaleRatio", serialization_alias="modelScaleRatio", default=1
    )
    max_roll_amplitude: Dimensional_Angle | None = Field(
        validation_alias="maxRollAmplitude", serialization_alias="maxRollAmplitude", default=None
    )
    min_roll_amplitude: Dimensional_Angle | None = Field(
        validation_alias="minRollAmplitude", serialization_alias="minRollAmplitude", default=None
    )
    heave_amplitude: Dimensional_Length | None = Field(
        validation_alias="heaveAmplitude", serialization_alias="heaveAmplitude", default=None
    )
    sway_amplitude: Dimensional_Length | None = Field(
        validation_alias="swayAmplitude", serialization_alias="swayAmplitude", default=None
    )
    damping_coefficient: float | None = Field(
        validation_alias="dampingCoefficient", serialization_alias="dampingCoefficient", default=1
    )
    time_period_for_liquid: Dimensional_Time | None = Field(
        validation_alias="timePeriodForLiquid", serialization_alias="timePeriodForLiquid", default=None
    )
    natural_period_of_ship: Dimensional_Time | None = Field(
        validation_alias="naturalPeriodOfShip", serialization_alias="naturalPeriodOfShip", default=None
    )
    reference_time_step: Dimensional_Time | None = Field(
        validation_alias="referenceTimeStep", serialization_alias="referenceTimeStep", default=None
    )
    increase_in_liquid_per_time_step: float | None = Field(
        validation_alias="increaseInLiquidPerTimeStep",
        serialization_alias="increaseInLiquidPerTimeStep",
        default=-0.001,
    )
