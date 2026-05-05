from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class AutomaticTimeStepDefintion(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC",
        description="Schema name: AutomaticTimeStepDefintion",
    )
    end_time: Dimensional_Time | None = Field(validation_alias="endTime", serialization_alias="endTime", default=None)
    initial_time_step: Dimensional_Time | None = Field(
        validation_alias="initialTimeStep", serialization_alias="initialTimeStep", default=None
    )
    minimum_time_step: Dimensional_Time | None = Field(
        validation_alias="minimumTimeStep", serialization_alias="minimumTimeStep", default=None
    )
    maximum_time_step: Dimensional_Time | None = Field(
        validation_alias="maximumTimeStep", serialization_alias="maximumTimeStep", default=None
    )
    physical_criteria: bool | None = Field(
        validation_alias="physicalCriteria",
        serialization_alias="physicalCriteria",
        default=False,
        description="Enable or disable user-defined criteria to control automatic time stepping adjustments during simulation.",
    )
    displacement_criteria: bool | None = Field(
        validation_alias="displacementCriteria",
        serialization_alias="displacementCriteria",
        default=False,
        description="Enable to limit time step based on displacement increment.",
    )
    displacement_increment: Dimensional_Length | None = Field(
        validation_alias="displacementIncrement", serialization_alias="displacementIncrement", default=None
    )
    total_strain_criteria: bool | None = Field(
        validation_alias="totalStrainCriteria",
        serialization_alias="totalStrainCriteria",
        default=False,
        description="Enable to limit time step based on total strain increment.",
    )
    total_strain_increment: Dimensional_Dimensionless | None = Field(
        validation_alias="totalStrainIncrement", serialization_alias="totalStrainIncrement", default=None
    )
    plastic_strain_criteria: bool | None = Field(
        validation_alias="plasticStrainCriteria",
        serialization_alias="plasticStrainCriteria",
        default=False,
        description="Enable to limit time step based on plastic strain increment.",
    )
    plastic_strain_increment: Dimensional_Dimensionless | None = Field(
        validation_alias="plasticStrainIncrement", serialization_alias="plasticStrainIncrement", default=None
    )
    stress_criteria: bool | None = Field(
        validation_alias="stressCriteria",
        serialization_alias="stressCriteria",
        default=False,
        description="Enable to limit time step based on stress increment.",
    )
    stress_increment: Dimensional_Pressure | None = Field(
        validation_alias="stressIncrement", serialization_alias="stressIncrement", default=None
    )
