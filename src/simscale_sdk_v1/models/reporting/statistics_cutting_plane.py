from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.vector3_d import Vector3D


class StatisticsCuttingPlane(SimScaleModel):
    """A cutting plane defined by a point and a normal vector. The plane is infinite and slices through the model geometry; statistics are computed over the resulting intersection."""

    identifier: str = Field(
        description="Unique label for this cutting plane. Used as the key for this plane's entry in the statisticsResult map returned when the report is finished."
    )
    position: Vector3D
    normal: Vector3D
