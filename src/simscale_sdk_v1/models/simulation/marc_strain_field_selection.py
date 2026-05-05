from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_strain_field_selection_strain_type import (
    OneOf_MarcStrainFieldSelectionStrainType,
)


class MarcStrainFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRAIN",
        description="Schema name: MarcStrainFieldSelection",
    )
    strain_type: OneOf_MarcStrainFieldSelectionStrainType | None = Field(
        validation_alias="strainType", serialization_alias="strainType", default=None
    )
