from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class ClockTimeWriteControl(SimScaleModel):
    """This option controls how the simulation results are written and how frequently."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CLOCK_TIME",
        description="This option controls how the simulation results are written and how frequently.  Schema name: ClockTimeWriteControl",
    )
    write_interval: Dimensional_Time | None = Field(
        validation_alias="writeInterval", serialization_alias="writeInterval", default=None
    )
