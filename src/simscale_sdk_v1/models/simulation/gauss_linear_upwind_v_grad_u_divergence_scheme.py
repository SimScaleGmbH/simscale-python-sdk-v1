from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class GaussLinearUpwindVGradUDivergenceScheme(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GAUSS_LINEARUPWINDV_GRAD_U_",
        description="Schema name: GaussLinearUpwindVGradUDivergenceScheme",
    )
