from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.incompressible_material import IncompressibleMaterial


class IncompressibleFluidMaterials(SimScaleModel):
    fluids: list[IncompressibleMaterial] | None = Field(default=None)
