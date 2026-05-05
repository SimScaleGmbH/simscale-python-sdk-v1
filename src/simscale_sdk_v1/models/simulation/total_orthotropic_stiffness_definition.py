from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__surface_tension import DimensionalVector_SurfaceTension


class TotalOrthotropicStiffnessDefinition(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_ORTHOTROPIC",
        description="Schema name: TotalOrthotropicStiffnessDefinition",
    )
    total: DimensionalVector_SurfaceTension | None = Field(default=None)
