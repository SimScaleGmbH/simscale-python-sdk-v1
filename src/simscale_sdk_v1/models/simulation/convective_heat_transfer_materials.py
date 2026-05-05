from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__convective_heat_transfer_materials_fluids import (
    OneOf_ConvectiveHeatTransferMaterialsFluids,
)


class ConvectiveHeatTransferMaterials(SimScaleModel):
    fluids: list[OneOf_ConvectiveHeatTransferMaterialsFluids] | None = Field(default=None)
