from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NumberIterationsWriteControl(SimScaleModel):
    """This option controls how the simulation results are written and how frequently."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NUMBER_OF_ITERATIONS_STEADY_STATE",
        description="This option controls how the simulation results are written and how frequently.  Schema name: NumberIterationsWriteControl",
    )
    write_interval: int | None = Field(
        validation_alias="writeInterval",
        serialization_alias="writeInterval",
        default=1000,
        description="Specify an interval value that defines the number of iterations between two writes of the result.",
    )
