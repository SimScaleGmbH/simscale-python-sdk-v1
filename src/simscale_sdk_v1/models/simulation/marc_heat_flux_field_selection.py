from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.marc_global_heat_flux_field_type import MarcGlobalHeatFluxFieldType


class MarcHeatFluxFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HEAT_FLUX",
        description="Schema name: MarcHeatFluxFieldSelection",
    )
    heat_flux_type: MarcGlobalHeatFluxFieldType | None = Field(
        validation_alias="heatFluxType", serialization_alias="heatFluxType", default=None
    )
