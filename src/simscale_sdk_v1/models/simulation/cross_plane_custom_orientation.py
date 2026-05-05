from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length


class CrossPlaneCustomOrientation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CROSS_PLANE",
        description="Schema name: CrossPlaneCustomOrientation",
    )
    cross_plane_orientation: DimensionalVector_Length | None = Field(
        validation_alias="crossPlaneOrientation", serialization_alias="crossPlaneOrientation", default=None
    )
