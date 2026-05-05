from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CustomFractionBodySurface(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_FRACTION_BODY_SURFACE",
        description="Schema name: CustomFractionBodySurface",
    )
    value: float | None = Field(default=0.696)
