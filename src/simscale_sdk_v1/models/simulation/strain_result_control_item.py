from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__strain_result_control_item_strain_type import (
    OneOf_StrainResultControlItemStrainType,
)


class StrainResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN",
        description="Schema name: StrainResultControlItem",
    )
    name: str | None = Field(default=None)
    strain_type: OneOf_StrainResultControlItemStrainType | None = Field(
        validation_alias="strainType", serialization_alias="strainType", default=None
    )
