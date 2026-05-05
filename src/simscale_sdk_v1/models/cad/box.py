from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Box(SimScaleModel):
    """Axis-aligned box."""

    min_x: float = Field(validation_alias="minX", serialization_alias="minX", description="Min x")
    min_y: float = Field(validation_alias="minY", serialization_alias="minY", description="Min y")
    min_z: float = Field(validation_alias="minZ", serialization_alias="minZ", description="Min z")
    max_x: float = Field(validation_alias="maxX", serialization_alias="maxX", description="Max x")
    max_y: float = Field(validation_alias="maxY", serialization_alias="maxY", description="Max y")
    max_z: float = Field(validation_alias="maxZ", serialization_alias="maxZ", description="Max z")
