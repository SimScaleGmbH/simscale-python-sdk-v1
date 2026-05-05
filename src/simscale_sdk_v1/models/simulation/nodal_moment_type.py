from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NodalMomentType(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="NODAL", description="Schema name: NodalMomentType"
    )
    component_selection: Literal["X", "Y", "Z", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
