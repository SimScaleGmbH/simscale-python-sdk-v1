from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SolidGlobalPhysics(SimScaleModel):
    enable_global_damping: bool | None = Field(
        validation_alias="enableGlobalDamping",
        serialization_alias="enableGlobalDamping",
        default=False,
        description="Apply a constant level of damping to all parts that do not have a specified material damping behavior.",
    )
    damping_level: float | None = Field(
        validation_alias="dampingLevel",
        serialization_alias="dampingLevel",
        default=1.0,
        description="Specify the level of damping to be applied globally as a percentage of critical damping.",
    )
