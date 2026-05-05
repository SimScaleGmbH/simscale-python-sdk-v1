from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.interpolation_parameters import InterpolationParameters


class MaterialUpdateOperationReference(SimScaleModel):
    """Reference identifiers of the provided material and its material group"""

    material_group_id: str | None = Field(
        validation_alias="materialGroupId",
        serialization_alias="materialGroupId",
        default=None,
        description="Identifier of the material group",
    )
    material_id: str | None = Field(
        validation_alias="materialId",
        serialization_alias="materialId",
        default=None,
        description="Identifier of the material",
    )
    interpolation_parameters: InterpolationParameters | None = Field(
        validation_alias="interpolationParameters", serialization_alias="interpolationParameters", default=None
    )
