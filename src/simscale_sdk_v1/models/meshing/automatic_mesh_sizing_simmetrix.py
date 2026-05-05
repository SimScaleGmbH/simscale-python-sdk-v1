from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__automatic_mesh_sizing_simmetrix_curvature import (
    OneOf_AutomaticMeshSizingSimmetrixCurvature,
)


class AutomaticMeshSizingSimmetrix(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC_V9",
        description="Schema name: AutomaticMeshSizingSimmetrix",
    )
    fineness: float | None = Field(
        default=5.0, description="Adjust the overall mesh sizing from coarse (value: 0) to fine (10)."
    )
    curvature: OneOf_AutomaticMeshSizingSimmetrixCurvature | None = Field(default=None)
