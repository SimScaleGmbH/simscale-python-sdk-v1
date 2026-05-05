from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class WindComfortSimulationControl(SimScaleModel):
    max_direction_run_time: Dimensional_Time | None = Field(
        validation_alias="maxDirectionRunTime", serialization_alias="maxDirectionRunTime", default=None
    )
    number_of_fluid_passes: float | None = Field(
        validation_alias="numberOfFluidPasses",
        serialization_alias="numberOfFluidPasses",
        default=3.0,
        description="Set how many times the fluid (air) passes over the domain during the simulation. Warning: Values below 2.0 might produce invalid results while higher numbers will require more simulation time and consequently more GPU hours. Recommended value is 3.0. Learn more.",
    )
    velocity_scaling: float | None = Field(
        validation_alias="velocityScaling",
        serialization_alias="velocityScaling",
        default=0.1,
        description="It affects the stability of the simulation. The default value of 0.1 is a good compromise between accuracy and computational requirements. Lower values of this parameter might increase the stability of the simulation at the cost of higher computational time.",
    )
