from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FaceNormalMagnetizationDirectionMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FACE_NORMAL",
        description="Schema name: FaceNormalMagnetizationDirectionMethod",
    )
    magnet_faces: TopologicalReference | None = Field(
        validation_alias="magnetFaces", serialization_alias="magnetFaces", default=None
    )
