from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GaussLinearUpwindLimitedGradDivergenceScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GAUSS_LINEARUPWIND_LIMITEDGRAD",
        description="Schema name: GaussLinearUpwindLimitedGradDivergenceScheme",
    )
