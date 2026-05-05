from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fluid_compressible_material import FluidCompressibleMaterial


class CompressibleFluidMaterials(SimScaleModel):
    fluids: list[FluidCompressibleMaterial] | None = Field(default=None)
