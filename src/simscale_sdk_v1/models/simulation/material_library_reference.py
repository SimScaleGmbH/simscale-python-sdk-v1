from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.interpolation_parameter import InterpolationParameter


class MaterialLibraryReference(SimScaleModel):
    material_group_id: str | None = Field(
        validation_alias="materialGroupId", serialization_alias="materialGroupId", default=None
    )
    material_id: str | None = Field(validation_alias="materialId", serialization_alias="materialId", default=None)
    interpolation_parameters: dict[str, InterpolationParameter] | None = Field(
        validation_alias="interpolationParameters", serialization_alias="interpolationParameters", default=None
    )
