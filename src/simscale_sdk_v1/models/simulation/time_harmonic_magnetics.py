from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__frequency import Dimensional_Frequency
from simscale_sdk_v1.models.simulation.one_of__time_harmonic_magnetics_time_dependency import (
    OneOf_TimeHarmonicMagneticsTimeDependency,
)


class TimeHarmonicMagnetics(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TIME_HARMONIC_MAGNETICS",
        description="Schema name: TimeHarmonicMagnetics",
    )
    frequency: Dimensional_Frequency | None = Field(default=None)
    thermal: bool | None = Field(
        default=False,
        description="Coupling with thermal solves for the temperature by considering electromagnetic losses such as Ohmic, hysteric or displacement losses.",
    )
    time_dependency: OneOf_TimeHarmonicMagneticsTimeDependency | None = Field(
        validation_alias="timeDependency", serialization_alias="timeDependency", default=None
    )
