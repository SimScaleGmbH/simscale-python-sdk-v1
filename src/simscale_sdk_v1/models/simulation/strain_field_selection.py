from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__strain_field_selection_strain_type import (
    OneOf_StrainFieldSelectionStrainType,
)


class StrainFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN",
        description="Schema name: StrainFieldSelection",
    )
    strain_type: OneOf_StrainFieldSelectionStrainType | None = Field(
        validation_alias="strainType", serialization_alias="strainType", default=None
    )
