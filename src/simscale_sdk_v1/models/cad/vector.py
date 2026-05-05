from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Vector(SimScaleModel):
    """3D vector."""

    x: float = Field(validation_alias="X", serialization_alias="X", description="X")
    y: float = Field(validation_alias="Y", serialization_alias="Y", description="Y")
    z: float = Field(validation_alias="Z", serialization_alias="Z", description="Z")
