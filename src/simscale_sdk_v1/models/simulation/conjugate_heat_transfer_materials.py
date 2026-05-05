from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fluid_compressible_material import FluidCompressibleMaterial
from simscale_sdk_v1.models.simulation.solid_compressible_material import SolidCompressibleMaterial


class ConjugateHeatTransferMaterials(SimScaleModel):
    fluids: list[FluidCompressibleMaterial] | None = Field(default=None)
    solids: list[SolidCompressibleMaterial] | None = Field(default=None)
