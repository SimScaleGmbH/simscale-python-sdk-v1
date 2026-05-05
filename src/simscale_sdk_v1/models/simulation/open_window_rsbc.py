from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__heat_flux import Dimensional_HeatFlux


class OpenWindowRSBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OPEN_WINDOW",
        description="Schema name: OpenWindowRSBC",
    )
    radiative_source_value: Dimensional_HeatFlux | None = Field(
        validation_alias="radiativeSourceValue", serialization_alias="radiativeSourceValue", default=None
    )
