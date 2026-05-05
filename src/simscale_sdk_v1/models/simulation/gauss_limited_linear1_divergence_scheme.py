from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GaussLimitedLinear1DivergenceScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GAUSS_LIMITEDLINEAR_1",
        description="Schema name: GaussLimitedLinear1DivergenceScheme",
    )
