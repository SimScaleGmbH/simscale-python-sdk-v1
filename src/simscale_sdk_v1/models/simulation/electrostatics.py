from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Electrostatics(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ELECTROSTATICS",
        description="Schema name: Electrostatics",
    )
    breakdown: bool | None = Field(
        default=False,
        description="Enabling allows the specification of the dielectric breakdown voltage for each material and the calculation of the safety factor.",
    )
