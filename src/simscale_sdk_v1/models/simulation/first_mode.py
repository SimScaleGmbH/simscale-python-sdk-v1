from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FirstMode(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="FIRSTMODE", description="Schema name: FirstMode"
    )
    number_of_modes: int | None = Field(
        validation_alias="numberOfModes",
        serialization_alias="numberOfModes",
        default=10,
        description="Define the maximum number of eigenfrequencies/eigenmodes, that should be calculated.",
    )
