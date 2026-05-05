from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__coupled_conjugate_heat_transfer_materials_fluids import (
    OneOf_CoupledConjugateHeatTransferMaterialsFluids,
)
from simscale_sdk_v1.models.simulation.solid_compressible_material import SolidCompressibleMaterial


class CoupledConjugateHeatTransferMaterials(SimScaleModel):
    fluids: list[OneOf_CoupledConjugateHeatTransferMaterialsFluids] | None = Field(default=None)
    solids: list[SolidCompressibleMaterial] | None = Field(default=None)
