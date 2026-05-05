from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GaussLimitedLinearV1DivergenceScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GAUSS_LIMITEDLINEARV_1",
        description="Schema name: GaussLimitedLinearV1DivergenceScheme",
    )
