from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MarcPrincipalPlasticStrainType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRINCIPAL_PLASTIC",
        description="Schema name: MarcPrincipalPlasticStrainType",
    )
    component_selection: Literal["MIN", "MID", "MAX", "ALL"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="ALL"
    )
