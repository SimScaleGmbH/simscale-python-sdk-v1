from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class RayleighDamping(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RAYLEIGH",
        description="Schema name: RayleighDamping",
    )
    stiffness_proportional_coefficient: Dimensional_Time | None = Field(
        validation_alias="stiffnessProportionalCoefficient",
        serialization_alias="stiffnessProportionalCoefficient",
        default=None,
    )
    mass_proportional_coefficient: Dimensional_Frequency | None = Field(
        validation_alias="massProportionalCoefficient", serialization_alias="massProportionalCoefficient", default=None
    )
