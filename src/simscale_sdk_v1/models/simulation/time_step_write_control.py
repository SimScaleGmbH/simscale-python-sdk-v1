from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TimeStepWriteControl(SimScaleModel):
    """This option controls how the simulation results are written and how frequently."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TIME_STEP",
        description="This option controls how the simulation results are written and how frequently.  Schema name: TimeStepWriteControl",
    )
    write_interval: int | None = Field(
        validation_alias="writeInterval",
        serialization_alias="writeInterval",
        default=None,
        description="Specify an interval value that defines the number of time steps between two writes of the result.",
    )
