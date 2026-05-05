from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MarcContactNormalStressType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NORMAL_STRESS",
        description="Schema name: MarcContactNormalStressType",
    )
    component_selection: Literal["X", "Y", "Z", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
