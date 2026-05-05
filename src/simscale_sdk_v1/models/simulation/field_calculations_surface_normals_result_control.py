from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.surface_normals_result_type import SurfaceNormalsResultType


class FieldCalculationsSurfaceNormalsResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_NORMALS",
        description="Schema name: FieldCalculationsSurfaceNormalsResultControl",
    )
    name: str | None = Field(default=None)
    result_type: SurfaceNormalsResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
