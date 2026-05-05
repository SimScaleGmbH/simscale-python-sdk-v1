from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.meshing.one_of__custom_mesh_sizing_simmetrix_curvature import (
    OneOf_CustomMeshSizingSimmetrixCurvature,
)


class CustomMeshSizingSimmetrix(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM",
        description="Schema name: CustomMeshSizingSimmetrix",
    )
    default_size: Dimensional_Length | None = Field(
        validation_alias="defaultSize", serialization_alias="defaultSize", default=None
    )
    min_size: Dimensional_Length | None = Field(validation_alias="minSize", serialization_alias="minSize", default=None)
    curvature: OneOf_CustomMeshSizingSimmetrixCurvature | None = Field(default=None)
