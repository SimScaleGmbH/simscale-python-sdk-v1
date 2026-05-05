from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless


class GreybodyDiffusiveRSBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GREYBODY_DIFFUSIVE",
        description="Schema name: GreybodyDiffusiveRSBC",
    )
    emissivity: Dimensional_Dimensionless | None = Field(default=None)
