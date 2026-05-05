from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.cube_root_vol_les_delta import CubeRootVolLesDelta


class SmoothLesDelta(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="SMOOTH", description="Schema name: SmoothLesDelta"
    )
    delta_coefficient: CubeRootVolLesDelta | None = Field(
        validation_alias="deltaCoefficient", serialization_alias="deltaCoefficient", default=None
    )
    max_delta_ratio: float | None = Field(
        validation_alias="maxDeltaRatio", serialization_alias="maxDeltaRatio", default=1.1
    )
