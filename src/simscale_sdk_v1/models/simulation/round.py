from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class Round(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="ROUND", description="Schema name: Round"
    )
    strand_diameter: Dimensional_Length | None = Field(
        validation_alias="strandDiameter", serialization_alias="strandDiameter", default=None
    )
