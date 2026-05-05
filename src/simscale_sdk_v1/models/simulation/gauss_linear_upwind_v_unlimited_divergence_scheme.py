from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GaussLinearUpwindVUnlimitedDivergenceScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GAUSS_LINEARUPWINDV_UNLIMITED",
        description="Schema name: GaussLinearUpwindVUnlimitedDivergenceScheme",
    )
    limiter_coefficient: float | None = Field(
        validation_alias="limiterCoefficient",
        serialization_alias="limiterCoefficient",
        default=1,
        description="This property defines a limiter coefficient for the scheme. 1 ensures boundedness while 0 applies no limiting.",
    )
