from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time
from simscale_sdk_v1.models.simulation.one_of__auto_timestep_definition_retiming_event import (
    OneOf_AutoTimestepDefinitionRetimingEvent,
)
from simscale_sdk_v1.models.simulation.restricted_dimensional_function__time import RestrictedDimensionalFunction_Time


class AutoTimestepDefinition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_V27",
        description="Schema name: AutoTimestepDefinition",
    )
    simulation_interval: Dimensional_Time | None = Field(
        validation_alias="simulationInterval", serialization_alias="simulationInterval", default=None
    )
    maximum_timestep_length: RestrictedDimensionalFunction_Time | None = Field(
        validation_alias="maximumTimestepLength", serialization_alias="maximumTimestepLength", default=None
    )
    minimum_timestep_length: Dimensional_Time | None = Field(
        validation_alias="minimumTimestepLength", serialization_alias="minimumTimestepLength", default=None
    )
    maximum_residual: float | None = Field(
        validation_alias="maximumResidual", serialization_alias="maximumResidual", default=10000000000
    )
    retiming_event: OneOf_AutoTimestepDefinitionRetimingEvent | None = Field(
        validation_alias="retimingEvent", serialization_alias="retimingEvent", default=None
    )
