from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class HystereticDamping(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HYSTERETIC",
        description="Schema name: HystereticDamping",
    )
    damping_level: float | None = Field(
        validation_alias="dampingLevel",
        serialization_alias="dampingLevel",
        default=1.0,
        description="Specify the level of damping to be applied as a percentage of critical damping.",
    )
