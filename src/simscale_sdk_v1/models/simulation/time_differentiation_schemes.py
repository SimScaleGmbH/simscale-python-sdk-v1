from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__time_differentiation_schemes_for_default import (
    OneOf_TimeDifferentiationSchemesForDefault,
)


class TimeDifferentiationSchemes(SimScaleModel):
    for_default: OneOf_TimeDifferentiationSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
    second_order_scheme: bool | None = Field(
        validation_alias="secondOrderScheme", serialization_alias="secondOrderScheme", default=False
    )
