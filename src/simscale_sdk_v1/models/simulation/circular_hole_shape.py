from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class CircularHoleShape(SimScaleModel):
    """Circular holes in the perforated plate."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CIRCULAR",
        description="Circular holes in the perforated plate.  Schema name: CircularHoleShape",
    )
    average_hole_diameter: Dimensional_Length | None = Field(
        validation_alias="averageHoleDiameter", serialization_alias="averageHoleDiameter", default=None
    )
