from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class SweepMeshingAbsoluteSize(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SWEEP_MESHING_ABSOLUTE_SIZE",
        description="Schema name: SweepMeshingAbsoluteSize",
    )
    thickness: Dimensional_Length | None = Field(default=None)
