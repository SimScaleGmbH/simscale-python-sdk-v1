from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__turbulent_dissipation import Dimensional_TurbulentDissipation


class InletOutletEBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_OUTLET",
        description="Schema name: InletOutletEBC",
    )
    value: Dimensional_TurbulentDissipation | None = Field(default=None)
