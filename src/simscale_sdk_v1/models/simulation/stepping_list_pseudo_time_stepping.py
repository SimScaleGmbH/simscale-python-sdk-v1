from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.restricted_dimensional_function__time import RestrictedDimensionalFunction_Time


class SteppingListPseudoTimeStepping(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STEPPING_LIST_V18",
        description="Schema name: SteppingListPseudoTimeStepping",
    )
    simulation_intervals: Dimensional_Time | None = Field(
        validation_alias="simulationIntervals", serialization_alias="simulationIntervals", default=None
    )
    timestep_length: RestrictedDimensionalFunction_Time | None = Field(
        validation_alias="timestepLength", serialization_alias="timestepLength", default=None
    )
