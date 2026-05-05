from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GaussLinearLimitedCorrectedLaplacianScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GAUSS_LINEAR_LIMITED_CORRECTED",
        description="Schema name: GaussLinearLimitedCorrectedLaplacianScheme",
    )
    limiter_coefficient: float | None = Field(
        validation_alias="limiterCoefficient",
        serialization_alias="limiterCoefficient",
        default=0.5,
        description="This property defines a limiter coefficient for the scheme:0: no correction, equivalent to the uncorrected scheme1: full non-orthogonal correction applied0.5: non-orthogonal contribution does not exceed the orthogonal part",
    )
