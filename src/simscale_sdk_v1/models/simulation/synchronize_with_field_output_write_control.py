from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SynchronizeWithFieldOutputWriteControl(SimScaleModel):
    """This option controls how the simulation results are written and how frequently."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTPUT_TIME",
        description="This option controls how the simulation results are written and how frequently.  Schema name: SynchronizeWithFieldOutputWriteControl",
    )
    write_interval: float | None = Field(
        validation_alias="writeInterval", serialization_alias="writeInterval", default=1
    )
