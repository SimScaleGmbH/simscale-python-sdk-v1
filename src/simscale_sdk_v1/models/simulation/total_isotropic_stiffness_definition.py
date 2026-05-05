from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__surface_tension import Dimensional_SurfaceTension


class TotalIsotropicStiffnessDefinition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_ISOTROPIC",
        description="Schema name: TotalIsotropicStiffnessDefinition",
    )
    total: Dimensional_SurfaceTension | None = Field(default=None)
