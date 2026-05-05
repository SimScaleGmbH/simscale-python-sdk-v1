from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__fixed_point_non_linearity_resolution_geometry_reactualization import (
    OneOf_FixedPointNonLinearityResolutionGeometryReactualization,
)


class FixedPointNonLinearityResolution(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_POINT",
        description="Schema name: FixedPointNonLinearityResolution",
    )
    geometry_reactualization: OneOf_FixedPointNonLinearityResolutionGeometryReactualization | None = Field(
        validation_alias="geometryReactualization", serialization_alias="geometryReactualization", default=None
    )
