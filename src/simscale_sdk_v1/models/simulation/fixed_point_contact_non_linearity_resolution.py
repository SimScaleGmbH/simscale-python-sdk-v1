from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__fixed_point_contact_non_linearity_resolution_iteration_control import (
    OneOf_FixedPointContactNonLinearityResolutionIterationControl,
)


class FixedPointContactNonLinearityResolution(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_POINT",
        description="Schema name: FixedPointContactNonLinearityResolution",
    )
    iteration_control: OneOf_FixedPointContactNonLinearityResolutionIterationControl | None = Field(
        validation_alias="iterationControl", serialization_alias="iterationControl", default=None
    )
