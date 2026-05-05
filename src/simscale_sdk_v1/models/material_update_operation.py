from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.material.material_response import MaterialResponse
from simscale_sdk_v1.models.material_update_operation_reference import MaterialUpdateOperationReference


class MaterialUpdateOperation(SimScaleModel):
    """Material update operation, which can be either updating an existing material in the spec, or adding a new one. See the `path` property to learn how add/update operations are distinguished."""

    path: str = Field(
        description="JSON pointer (considering the `model` field as root) specifying where to add the material. If it points to a container (e.g. `/materials` or `/materials/solids`), the material will be added to that container. If it points to an existing material instead (e.g. `/materials/0` or `/materials/solids/0`), the new material will replace the one the pointer points to."
    )
    material_data: MaterialResponse = Field(validation_alias="materialData", serialization_alias="materialData")
    material_spec: dict[str, Any] | None = Field(
        validation_alias="materialSpec",
        serialization_alias="materialSpec",
        default=None,
        description="Material spec object that will be used as the base to apply the physical properties passed in `materialData`.",
    )
    reference: MaterialUpdateOperationReference | None = Field(default=None)
    material_data_sources: list[Literal["MATERIAL_LIBRARY_DATA", "SPEC_DATA", "SCHEMA_DEFAULT"]] | None = Field(
        validation_alias="materialDataSources",
        serialization_alias="materialDataSources",
        default=["MATERIAL_LIBRARY_DATA", "SPEC_DATA"],
    )
