from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__length import DimensionalFunction_Length


class WithFictitiousClearance(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WITH_FICTITIOUS_CLEARANCE",
        description="Schema name: WithFictitiousClearance",
    )
    master_clearance: DimensionalFunction_Length | None = Field(
        validation_alias="masterClearance", serialization_alias="masterClearance", default=None
    )
    slave_clearance: DimensionalFunction_Length | None = Field(
        validation_alias="slaveClearance", serialization_alias="slaveClearance", default=None
    )
