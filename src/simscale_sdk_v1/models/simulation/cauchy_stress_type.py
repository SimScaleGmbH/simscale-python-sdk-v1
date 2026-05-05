from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CauchyStressType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CAUCHY",
        description="Schema name: CauchyStressType",
    )
    component_selection: Literal["XX", "YY", "ZZ", "XY", "XZ", "YZ", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
