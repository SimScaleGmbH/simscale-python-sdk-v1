from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FrictionVelocityResultType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRICTION_VELOCITY_U_TAU",
        description="Schema name: FrictionVelocityResultType",
    )
