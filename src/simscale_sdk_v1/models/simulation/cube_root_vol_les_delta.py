from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CubeRootVolLesDelta(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUBE_ROOT_VOL",
        description="Schema name: CubeRootVolLesDelta",
    )
    delta_coefficient: float | None = Field(
        validation_alias="deltaCoefficient", serialization_alias="deltaCoefficient", default=1
    )
