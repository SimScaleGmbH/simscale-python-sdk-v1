from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OutputSteps(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTPUT_STEPS",
        description="Schema name: OutputSteps",
    )
    number_of_output_steps: int | None = Field(
        validation_alias="numberOfOutputSteps",
        serialization_alias="numberOfOutputSteps",
        default=20,
        description="Specify the number of output steps for the entire simulation. They are distributed as evenly as possible.",
    )
