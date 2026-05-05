from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FullResolutionTDBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FULL_RESOLUTION",
        description="Schema name: FullResolutionTDBC",
    )
    prandtl_number: float | None = Field(
        validation_alias="prandtlNumber", serialization_alias="prandtlNumber", default=0.85
    )
