from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NoFriction(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NO_FRICTION",
        description="Schema name: NoFriction",
    )
