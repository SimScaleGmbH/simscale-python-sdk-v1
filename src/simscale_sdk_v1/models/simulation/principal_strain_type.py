from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PrincipalStrainType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRINCIPAL",
        description="Schema name: PrincipalStrainType",
    )
    component_selection: Literal["FIRST_COMPONENT", "SECOND_COMPONENT", "THIRD_COMPONENT", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
