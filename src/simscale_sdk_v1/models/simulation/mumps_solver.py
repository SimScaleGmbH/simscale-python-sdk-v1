from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_mumps_settings import AdvancedMUMPSSettings


class MUMPSSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="MUMPS", description="Schema name: MUMPSSolver"
    )
    advanced_mumps_settings: AdvancedMUMPSSettings | None = Field(
        validation_alias="advancedMumpsSettings", serialization_alias="advancedMumpsSettings", default=None
    )
